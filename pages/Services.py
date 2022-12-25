# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 23:36:04 2022

@author: dludwinski
"""

import streamlit as st
from pathlib import Path, PurePath
import sys
sys.path.append(str(Path(PurePath(__file__).parents[1], '__helpers__')))
from  __return_centered_email_address__ import _return_centered_email
from __sm_links__ import _display_sm_links
from __add_pages_links__ import _display_pages_links
from __get_image_to_display__ import (
    return_image_from_path,
    return_image_from_path_and_resize_medium
    )

FONT = 'Nanum Gothic'
FONT1 = 'Papyrus'


@st.cache(suppress_st_warning=True)
def _return_services_with_display() -> dict:
    data_path = Path(
        PurePath(__file__).parents[1],
        PurePath('.data/.database/services')
    )
    brand_logo = Path(
        data_path,
        'Brand Building & Logo Creation.png'
        )
    se_display = Path(
        data_path,
        'From Unknown to Known.png'
        )
    logo_display = Path(
        data_path,
        'Recruiting Made Simple.png'
        )
    wa_display = Path(
        data_path,
        'Data Analytics & Web App Creation.png'
        )
    return {
        str(brand_logo.name): return_image_from_path_and_resize_medium(
            brand_logo
            ),
        str(se_display.name): return_image_from_path_and_resize_medium(
            se_display
            ),
        str(logo_display.name): return_image_from_path_and_resize_medium(
            logo_display
            ),
        str(wa_display.name): return_image_from_path_and_resize_medium(
            wa_display
            ),
    }


def _services_page_func() -> None:
    services = _return_services_with_display()
    st.markdown(
        f"<h1 style='text-align: center; font-family: {FONT};'>\
        Services<h2>",
        unsafe_allow_html=True,
        )
    with st.container():
        col1, col2 = st.columns([2, 2])
        for i, (service, view) in enumerate(services.items()):
            if (i % 2) != 0:
                col1.image(view, caption=service, use_column_width='always')
            else:
                col2.image(view, caption=service, use_column_width='always')


def services_page_main():
    global FONT, FONT1
    import Contacts
    logo_path = str(
        Path(PurePath(__file__).parents[1],
             '.data', 'images', 'Logo', 'The Social Outfit.png'
             )
    )
    st.set_page_config(
        layout='wide',
        page_title='The Social Outfit - Services',
        page_icon=return_image_from_path(logo_path),
        menu_items=None,
        initial_sidebar_state='collapsed',
        )
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                div.block-container {padding-top:1rem; padding-bottom:0rem;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    _services_page_func()
    st.markdown('<p><br></p>', unsafe_allow_html=True)
    with st.expander('Send Us a Message:'):
        Contacts._email_form_func()
    with st.container():
        _return_centered_email()
    with st.container():
        _display_sm_links()
    with st.container():
        _display_pages_links()


if __name__ == '__main__':
    services_page_main()
