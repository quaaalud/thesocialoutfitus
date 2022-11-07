# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:30:24 2022

@author: dludwinski
"""

import streamlit as st


def _get_portofolio_contents(file_type: str) -> dict:
    import __pathconstants__ as _paths
    dirname = _paths.get_directory_path(file_type)
    try:
        dirlist = dirname.iterdir()

    except FileNotFoundError:
        import os
        os.mkdir(str(dirname))
    dirlist = dirname.iterdir()
    sorted_dirs = sorted(dirlist, key=lambda t: -t.lstat().st_mtime)
    return {
        i: _file for i, _file in
        enumerate(list(sorted_dirs))
    }


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


def _assign_data_to_tab(tab_name, _title, _func):
    with tab_name:
        st.subheader(_title)
        st.write(_func)


def portfolio_page_main():
    st.header('Portfolio')
    st.subheader('Recent Projects:')
    for _file in _display_newest_files():
        st.write(_file)
    ani_tab, img_tab, msc_tab, vdo_tab = st.tabs([
        'Animations', 'Images', 'Music', 'Videos'
    ])
    _assign_data_to_tab(ani_tab, 'Animations', _return_animations())
    _assign_data_to_tab(img_tab, 'Images', _return_images())
    _assign_data_to_tab(msc_tab, 'Music', _return_music())
    _assign_data_to_tab(vdo_tab, 'Videos', _return_videos())


if __name__ == '__main__':
    portfolio_page_main()
