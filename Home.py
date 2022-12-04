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

FONT = 'Nanum Gothic'
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
    city_logo = str(
        Path(IMG_PATH, 'Logo', 'The Social Outfit.png'))
    car_path = str(Path(IMG_PATH, 'Demo 1.jpg'))
    city_path = str(Path(IMG_PATH, 'Demo 5.jpg'))
    bw_path = str(Path(IMG_PATH, 'Demo 4.jpg'))
    st.set_page_config(
        layout='wide',
        page_title='The Social Outfit - Home',
        page_icon=return_image_from_path(logo_path),
        menu_items=None,
        initial_sidebar_state='collapsed',
        )
    # Hide mainmenu and footer
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    add_bg.add_bg_from_local(white_logo)
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    with st.container():
        with st.container():
            col1, col2, col3 = st.columns([.5, 1.5, .5])
            col1.empty()
            col2.image(return_image_from_path(str(city_logo)))
            col3.empty()
    st.empty()
#    st.markdown(
#        f"<h1 style='text-align: center; font-family: {FONT};'> \
#        Welcome to The Social Outfit</h1>",
#        unsafe_allow_html=True
#        )
    st.empty()
#    st.markdown(
#        f"<h2 style='text-align: center; font-family:{FONT};'> \
#        Value creation for all things brand or business. </h2>",
#        unsafe_allow_html=True
#        )
    with st.expander('Contact Us Today'):
        Contacts._email_form_func()
#    with st.expander('Take a look at what we can do for you'):
    with st.container():
        Portfolio._portfolio_page_func()
    with st.container():
#    with st.expander('See the current services offered'):
        Services._services_page_func()


if __name__ == '__main__':
    main()
