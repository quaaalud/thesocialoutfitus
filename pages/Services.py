# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 23:36:04 2022

@author: dludwinski
"""

import streamlit as st
from pathlib import Path, PurePath
import sys
sys.path.append(str(Path(PurePath(__file__).parents[1], '__helpers__')))
import __add_background_from_local__ as add_bg

FONT = 'Ink Free'
FONT1 = 'Papyrus'


def _return_services_with_display() -> dict:
    from __get_image_to_display__ import return_image_from_path
    data_path = Path(
        PurePath(__file__).parents[1],
        PurePath('.data')
    )
    media_display = Path(data_path,
                         'images/Logo/Social Outfit Logo.png'
                         )
    se_display = Path(data_path,
                      'images/Logo/Social Outfit Logo All White.png'
                      )
    logo_display = Path(data_path,
                        'images/Logo/Social Outfit Logo.png'
                        )
    wa_display = Path(data_path,
                      'images/Logo/Social Outfit Logo All White.png'
                      )
    return {
        'Build your Social Media Presence': return_image_from_path(
            media_display
            ),
        'Search Engine Optimization': return_image_from_path(
            se_display
            ),
        'Logo Creation': return_image_from_path(
            logo_display
            ),
        'Simple Web App Creation': return_image_from_path(
            wa_display
            ),
    }


def services_page_main():
    global FONT, FONT1
    try:
        st.set_page_config(
            layout="wide",
            page_title='The Social Outfit - Services',
            )
    except:
        pass
    services = _return_services_with_display()
    st.header('Services Offered')
    i = 0
    for service, view in services.items():
        if (i % 2) == 0:
            col1, col2 = st.columns(2)
            col1.markdown(
                f"<h2 style='text-align: center; font-family: {FONT};'> \
                {service}<h2>",
                unsafe_allow_html=True,
                )
            col2.image(view)
            i += 1
        else:
            col1, col2 = st.columns(2)
            col1.image(view)
            col2.markdown(
                f"<h2 style='text-align: center; font-family: {FONT};'> \
                {service}<h2>",
                unsafe_allow_html=True,
                )
            i += 1


if __name__ == '__main__':
    services_page_main()
