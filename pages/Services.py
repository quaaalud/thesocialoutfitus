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
from __get_header_gif__ import _return_gif_html
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
    lead_display = Path(
        data_path,
        'Lead Generation.gif'
        )
    rec_display = Path(
        data_path,
        'Recruiting & Retention.png'
        )
    wa_display = Path(
        data_path,
        'Data Analytics & Web App Creation.png'
        )
    tag_display = Path(
        data_path,
        'The Social Outfit Tagline.png'
        )
    return {
        str(brand_logo.name): return_image_from_path_and_resize_medium(
            brand_logo
            ),
        str(tag_display.name): return_image_from_path_and_resize_medium(
            tag_display
            ),
        str(rec_display.name): return_image_from_path_and_resize_medium(
            rec_display
            ),
        str(wa_display.name): return_image_from_path_and_resize_medium(
            wa_display
            ),
        str(lead_display.name): _return_gif_html(
            lead_display
            ),
    }


def _services_page_func() -> None:
    services = _return_services_with_display()
    with st.container():
        col1, col2 = st.columns([2, 2])
        e1, single_col, e2 = st.columns([1, 2, 1])
        for i, (service, view) in enumerate(services.items()):
            if 'gif' not in service:
                if i < 4:  
                    if (i % 2) != 0:
                        col1.image(
                            view, 
                            use_column_width='always'
                            )
                    else:
                        col2.image(
                            view, 
                            use_column_width='always'
                            )
            else:
                single_col.markdown(
                    view,
                    unsafe_allow_html=True,
                )
                


def services_page_main():
    global FONT, FONT1
    import Contacts
    logo_path = str(
        Path(PurePath(__file__).parents[1],
             '.data', 'images', 'Logo', 'The Social Outfit.png'
             )
    )
    IMG_PATH = str(
        Path(PurePath(__file__).parents[1],
             '.data', '.database', 'bg_images', 
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
    page_head = str(
        Path(IMG_PATH, 'services-header.png')
        )
    col1, col2, col3 = st.columns([2, 3, 2])
    col2.image(return_image_from_path(page_head),
               use_column_width=True,
               )
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
    col1, col2, col3 = st.columns([2.5, 5, 2.5])
    main_logo_gif = str(
        Path(Path(__file__).parents[1],
             '.data',
             'images',
             'Logo',
             'tso_logo_loop.gif'
             )
    )
    col1, col2, col3 = st.columns([2.5, 5, 2.5])
    col2.markdown(
        _return_gif_html(main_logo_gif),
        unsafe_allow_html=True,
    )


if __name__ == '__main__':
    services_page_main()
