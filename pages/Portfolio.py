# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:30:24 2022

@author: dludwinski
"""

import streamlit as st
from pathlib import Path, PurePath
import sys
sys.path.append(str(Path(PurePath(__file__).parents[1], '__helpers__')))
import __add_background_from_local__ as add_bg
from __get_image_to_display__ import return_image_from_path

FONT = 'Ink Free'
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
    i = 0
    for name, img in img_dict.items():
        with img_tab:
            cols = [col for col in st.columns(len([img_dict.keys()]))]
            with st.container():
                for col in [col for col in cols]:
                    if (i % 2) == 0:
                        col1, col2 = st.columns(2)
                        col1.image(return_image_from_path(img))
                        col2.markdown(
                            f"\
            <p style='text-align: left; font-family: {FONT};'>{str(name)}</p>",
                            unsafe_allow_html=True,
                            )
                        i += 1
                    else:
                        col1, col2 = st.columns(2)
                        col1.markdown(
                            f"\
            <p style='text-align: left; font-family: {FONT};'>{str(name)}</p>",
                            unsafe_allow_html=True,
                            )
                        col2.image(return_image_from_path(img))
                        i += 1


def _assign_videos_to_tab(vdo_tab: st.tabs) -> st.video:
    vid_types = ['.mp4', '.ogg', '.mov']
    all_videos = {name: vid for name, vid in _return_videos().items() if
                  Path(vid).suffix in vid_types}
    i = 0
    for name, vid in all_videos.items():
        with vdo_tab:
            cols = [col for col in st.columns(len([all_videos.keys()]))]
            with st.container():
                for col in [col for col in cols]:
                    if (i % 2) == 0:
                        col1, col2 = st.columns(2)
                        col1.video(open(vid, 'rb'))
                        col2.markdown(
                            f"\
            <p style='text-align: left; font-family: {FONT};'>{str(name)}</p>",
                            unsafe_allow_html=True,
                            )
                        i += 1
                    else:
                        col1, col2 = st.columns(2)
                        col1.markdown(
                            f"\
            <p style='text-align: left; font-family: {FONT};'>{str(name)}</p>",
                            unsafe_allow_html=True,
                            )
                        col2.video(open(vid, 'rb'))
                        i += 1


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
    <p style='text-align: left; font-family: {FONT};'>{str(song_name)}</p>",
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
        f"<h1 style='text-align: center; font-family: {FONT};'>\
        Portfolio</h1>",
        unsafe_allow_html=True
        )
    st.markdown(
        f"<h2 style='text-align: left; font-family: {FONT};'>\
        Recent Projects</h1>",
        unsafe_allow_html=True
        )
    ani_tab, img_tab, msc_tab, vdo_tab = st.tabs([
        'Animations', 'Images', 'Music', 'Videos'
    ])
    _assign_data_to_tab(ani_tab, 'Animations', _return_animations)
    _assign_images_to_tab(img_tab)
    _assign_music_to_tab(msc_tab)
    _assign_videos_to_tab(vdo_tab)


def portfolio_page_main():
    import Contacts
    logo_path = str(
        Path(PurePath(__file__).parents[1],
             '.data', 'images', 'Logo', 'Social Outfit Logo.png'
             )
        )
    st.set_page_config(
        layout="wide",
        page_title='The Social Outfit - Portfolio',
        page_icon=return_image_from_path(logo_path),
        )
    _portfolio_page_func()
    with st.expander('Send Us a Message:'):
        Contacts._email_form_func()


if __name__ == '__main__':
    portfolio_page_main()
