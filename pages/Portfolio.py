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
                        col2.caption(name)
                        i += 1
                    else:
                        col1, col2 = st.columns(2)
                        col2.caption(name)
                        col2.video(open(vid, 'rb'))
                        i += 1



def _assign_music_to_tab(msc_tab: st.tabs) -> st.audio:
    file_types_dict = {
        '.mp3': 'audio/mp3',
        '.ogg': 'audio/ogg',
        '.wav': 'audio/wav',
    }
    all_music = _return_music()
    for song_name, file_path in all_music.items():
        if str(file_path.suffix) in file_types_dict.keys():
            with msc_tab:
                st.subheader(str(song_name))
                st.audio(
                    str(file_path),
                    file_types_dict.get(str(file_path.suffix))
                    )


def portfolio_page_main():
    logo_path = Path(
        PurePath(__file__).parents[1],
        PurePath('.data/images/Logo')
    )
    #add_bg.add_bg_from_local(str(Path(logo_path, 'Social Outfit Logo.png')))
    st.header('Portfolio')
    st.subheader('Recent Projects:')
    for _file in _display_newest_files():
        st.write(_file)
    ani_tab, img_tab, msc_tab, vdo_tab = st.tabs([
        'Animations', 'Images', 'Music', 'Videos'
    ])
    _assign_data_to_tab(ani_tab, 'Animations', _return_animations)
    _assign_data_to_tab(img_tab, 'Images', _return_images)
    _assign_music_to_tab(msc_tab)
    _assign_videos_to_tab(vdo_tab)


if __name__ == '__main__':
    portfolio_page_main()
