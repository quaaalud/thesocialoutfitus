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
sys.path.append(str(Path(PurePath(__file__).parent, '__helpers__')))

from __get_image_to_display__ import return_image_from_path
from  __return_centered_email_address__ import _return_centered_email
from __sm_links__ import _display_sm_links
from __add_pages_links__ import _display_pages_links
from __get_header_gif__ import _return_gif_html

FONT = 'Nanum Gothic'
FONT1 = 'Papyrus'

def main():
    logo_path = str(
        Path(PurePath(__file__).parents[0],
             '.data', 'images', 'Logo', 'The Social Outfit.png'
             )
    )
    st.set_page_config(
        layout='wide',
        page_title='The Social Outfit - Home',
        page_icon=return_image_from_path(logo_path),
        menu_items=None,
        initial_sidebar_state='collapsed',
        )
    global FONT, FONT1, DATA_PATH, IMG_PATH
    import Contacts
    import Portfolio
    import Services
    # Hide mainmenu and footer
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                div.block-container {padding-top:1rem; padding-bottom:0rem;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    white_logo = str(
        Path(IMG_PATH, 'Logo', 'Social Outfit Logo All White Slim.png')
        )
    empty1 = st.empty()
    with st.container():
        with st.container():
            col1, col2, col3 = st.columns([2, 5, 2])
            col1.empty()
            col2.image(
                return_image_from_path(white_logo),
                use_column_width=True,
                )
            col3.empty()
    break_line = '<p> <br></p>'
    
    with st.expander('Contact Us Today'):
        Contacts._email_form_func()
    st.markdown(break_line, unsafe_allow_html=True)
    with st.container():
        Services._services_page_func()
    st.markdown(break_line, unsafe_allow_html=True)
    with st.container():
        _return_centered_email()
    st.markdown(break_line, unsafe_allow_html=True)
    with st.container():
        _display_sm_links()
    with st.container():
        _display_pages_links()
    empty1.header(' ')


if __name__ == '__main__':
    main()
