# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:30:24 2022

@author: dludwinski
"""

import streamlit as st
import base64
from pathlib import Path, PurePath
import sys
sys.path.append(str(Path(PurePath(__file__).parents[1], '__helpers__')))
import __add_background_from_local__ as add_bg
from __get_image_to_display__ import return_image_from_path

FONT = 'Nanum Gothic'
FONT1 = 'Papyrus'


def _get_portofolio_contents(file_type: str) -> dict:
    import __pathconstants__ as _paths
    dirname = _paths.get_directory_path(file_type)
    try:
        dirlist = dirname.iterdir()

    except FileNotFoundError:
        import os
        os.mkdir(str(dirname))
    dirlist = [_file for _file in dirname.iterdir()
               if _file.is_file()
               ]
    sorted_dirs = sorted(dirlist, key=lambda t: -t.lstat().st_mtime)
    file_names = [_file.name.split('.')[0] for _file in sorted_dirs]
    return dict(zip(file_names, sorted_dirs))


def _return_animations() -> dict:
    return _get_portofolio_contents('animations')


def _return_images() -> dict:
    return _get_portofolio_contents('images')


def _return_music() -> dict:
    return _get_portofolio_contents('music')


def _return_videos() -> dict:
    return _get_portofolio_contents('videos')


def _display_newest_files() -> list:
    import __pathconstants__ as _paths
    newest_files = {}
    filetypes = _paths.__PATHS__().return_portfolio_directories()
    for file_type in filetypes:
        try:
            newest_files[file_type] = (
                _get_portofolio_contents(file_type)[0]
            )
        except KeyError:
            newest_files[file_type.capitalize()] = (
                ''
            )
    return newest_files


def _assign_data_to_tab(tab_name, _title, _retfunc):
    with tab_name:
        st.subheader(_title)
        st.write(_retfunc())


def _assign_images_to_tab(img_tab: st.tabs) -> st.image:
    img_dict = _return_images()
    for name, img in img_dict.items():
        with img_tab:
            cols = [col for col in st.columns(len([img_dict.keys()]))]
            with st.container():
                for col in [col for col in cols]:
                    col1, col2 = st.columns([1, 2])
                    col1.markdown(
                        f"\
        <h2 style='text-align: left; font-family: {FONT};'>{str(name)}</h2>",
                        unsafe_allow_html=True,
                        )
                    col2.image(return_image_from_path(img))


def _assign_videos_to_tab() -> st.video:
    vid_types = ['.mp4', '.ogg', '.mov']
    all_videos = {name: vid for name, vid in _return_videos().items() if
                  str(Path(vid).suffix).lower() in vid_types}
    for name, vid in all_videos.items():
        with st.container():
            cols = [col for col in st.columns(len([all_videos.keys()]))]
            for col in [col for col in cols]:
                col1, col2 = st.columns([1, 2])
                col1.markdown(
                    f"\
    <h2 style='text-align: left; font-family: {FONT};'>{str(name)}</h2>",
                    unsafe_allow_html=True,
                    )
                col2.video(open(vid, 'rb'))


def _assign_animations_to_tab() -> None:
    gif_files = {
        name: gif for name, gif in _return_animations().items() if
        'gif' in str(Path(gif).suffix).lower()
        }
    i = 0
    for name, gif in gif_files.items():
        with st.container():
            cols = [col for col in st.columns(len([gif_files.keys()]))]
            for col in [col for col in cols]:
                file_ = open(str(gif), "rb")
                contents = file_.read()
                data_url = base64.b64encode(contents).decode("utf-8")
                file_.close()
                col1, col2 = st.columns(2)
                col1.markdown(
                    f"\
    <h2 style='text-align: left; font-family: {FONT};'>{str(name)}</h2>",
                    unsafe_allow_html=True,
                    )
                col2.markdown(
                    f'<img src="data:image/gif;base64,{data_url}">',
                    unsafe_allow_html=True,
                    )


def _assign_music_to_tab(msc_tab: st.tabs) -> st.audio:
    global FONT
    file_types_dict = {
        '.mp3': 'audio/mp3',
        '.ogg': 'audio/ogg',
        '.wav': 'audio/wav',
    }
    all_music = _return_music()
    for song_name, file_path in all_music.items():
        if str(file_path.suffix) in file_types_dict.keys():
            with msc_tab:
                st.markdown(
                    f"\
    <h2 style='text-align: left; font-family: {FONT};'>{str(song_name)}</h2>",
                    unsafe_allow_html=True,
                    )
                st.audio(
                    str(file_path),
                    file_types_dict.get(str(file_path.suffix))
                    )


def _portfolio_page_func():
    global FONT
#    add_bg.add_bg_from_local(str(Path(logo_path, 'Social Outfit Logo.png')))
    st.markdown(
        f"<h1 style='text-align: center; font-family: {FONT}; color:#EDEDED;'>\
        Portfolio</h1>",
        unsafe_allow_html=True
        )
    st.markdown(
        f"<h2 style='text-align: left; font-family: {FONT};'>\
        Recent Projects</h1>",
        unsafe_allow_html=True
        )
    img_tab, msc_tab, vdo_tab = st.tabs([
        'Logos & Photography', 'Music & Sounds', 'Videos & Animation'
    ])
    _assign_images_to_tab(img_tab)
    _assign_music_to_tab(msc_tab)
    with vdo_tab:
        _assign_animations_to_tab()
        _assign_videos_to_tab()


def portfolio_page_main():
    import Contacts
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    logo_path = str(
        Path(PurePath(__file__).parents[1],
             '.data', 'images', 'Logo', 'Social Outfit Logo.png'
             )
        )
    try:
        st.set_page_config(
            layout="wide",
            page_title='The Social Outfit - Portfolio',
            page_icon=return_image_from_path(logo_path),
            )
    except:
        pass
    _portfolio_page_func()
    with st.expander('Send Us a Message:'):
        Contacts._email_form_func()


if __name__ == '__main__':
    portfolio_page_main()
