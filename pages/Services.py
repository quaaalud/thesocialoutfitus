# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 23:36:04 2022

@author: dludwinski
"""

import streamlit as st
from pathlib import Path, PurePath
import sys
sys.path.append(str(Path(PurePath(__file__).parents[1], '__helpers__')))
from __get_image_to_display__ import return_image_from_path

FONT = 'Nanum Gothic'
FONT1 = 'Papyrus'


@st.cache(suppress_st_warning=True)
def _return_services_with_display() -> dict:
    from __get_image_to_display__ import return_image_from_path
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
        str(brand_logo.name): return_image_from_path(
            brand_logo
            ),
        str(se_display.name): return_image_from_path(
            se_display
            ),
        str(logo_display.name): return_image_from_path(
            logo_display
            ),
        str(wa_display.name): return_image_from_path(
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
    try:
        st.set_page_config(
            layout="centered",
            page_title='The Social Outfit - Services',
            page_icon=return_image_from_path(
                str(
                    Path(
                        Path(__file__).parents[1], 
                        '.data', 
                        '.database',
                        'services', 
                        'Data Analytics & Web App Creation.png'
                        )
                    )
                )
            )
    except st.errors.StreamlitAPIException:
        pass
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    _services_page_func()
    with st.expander('Send Us a Message:'):
        Contacts._email_form_func()


if __name__ == '__main__':
    services_page_main()
