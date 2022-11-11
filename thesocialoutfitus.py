# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:16:22 2022

@author: dludwinski
"""

import streamlit as st
from pathlib import PurePath, Path
import sys

DATA_PATH = Path(PurePath(__file__).parent, '.data')
IMG_PATH = Path(DATA_PATH, 'images')
sys.path.append(str(DATA_PATH))
sys.path.append(str(Path(PurePath(__file__).parent, 'pages')))


def main():
    import Contacts
    import Portfolio
    import __add_background_from_local__ as add_bg
    global DATA_PATH, IMG_PATH
    logo_path = Path(IMG_PATH, 'Logo')
    add_bg.add_bg_from_local(str(Path(logo_path, 'Social Outfit Logo.png')))

    st.header('Welcome to The Social Outfit')
    with st.container():
        st.subheader(
            "Saving you time so your business can do what it's best at!"
        )


def _get_db_connection():
    import __pathconstants__
    import __createdatabase__


if __name__ == '__main__':
    main()
