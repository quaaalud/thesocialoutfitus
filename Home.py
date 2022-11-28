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

FONT = 'Ink Free'
FONT1 = 'Papyrus'

def main():
    global FONT, FONT1
    import Contacts
    import Portfolio
    import Services
    import __add_background_from_local__ as add_bg
    from __get_image_to_display__ import return_image_from_path
    global DATA_PATH, IMG_PATH
    logo_path = str(Path(IMG_PATH, 'Logo', 'Social Outfit Logo.png'))
    white_logo = str(
        Path(IMG_PATH, 'Logo', 'Social Outfit Logo All White.png'))
    st.set_page_config(
        layout='wide',
        page_title='The Social Outfit',
        page_icon=logo_path,
        menu_items=None,
        initial_sidebar_state='collapsed',
        )
    with st.container():
        with st.container():
            col1, col2, col3 = st.columns(3)
            col1.image(return_image_from_path(str(logo_path)))
            col2.image(return_image_from_path(str(white_logo)))
            col3.image(return_image_from_path(str(logo_path)))
        with st.container():
            col1, col2, col3 = st.columns(3)
            col1.image(return_image_from_path(str(white_logo)))
            col2.image(return_image_from_path(str(logo_path)))
            col3.image(return_image_from_path(str(white_logo)))
        with st.container():
            col1, col2, col3 = st.columns(3)
            col1.image(return_image_from_path(str(logo_path)))
            col2.image(return_image_from_path(str(white_logo)))
            col3.image(return_image_from_path(str(logo_path)))
    st.empty()
    st.markdown(
        f"<h1 style='text-align: center; font-family: {FONT};'> \
        Welcome to The Social Outfit</h1>",
        unsafe_allow_html=True
        )
    st.empty()
    st.markdown(
        f"<h2 style='text-align: center; font-family:{FONT1};'> \
        Saving you time so your business can do what it's best at!</h2>",
        unsafe_allow_html=True
        )
    with st.expander('Contact Us Today'):
        Contacts.contacts_page_main()
    with st.expander('Take a look at what we can do for you'):
        Portfolio._portfolio_page_func()
    with st.expander('See the current services offered'):
        Services.services_page_main()


def _get_db_connection():
    import __pathconstants__
    import __createdatabase__


if __name__ == '__main__':
    main()
