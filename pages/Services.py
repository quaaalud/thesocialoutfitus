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
from __get_image_to_display__ import return_image_from_path

FONT = 'Nanum Gothic'
FONT1 = 'Papyrus'


def _return_services_with_display() -> dict:
    from __get_image_to_display__ import return_image_from_path
    data_path = Path(
        PurePath(__file__).parents[1],
        PurePath('.data')
    )
    media_description = """\
Custom Content created for your
Business or Platform ranging from
Simple Jingles to Full Commercials
allowing you to focus on providing
quality Services and Products
"""
    seo_description = """\
Providing Search Engine Optimization
(SEO) ensures potential customers
see how you can help them as reports
show average consumers never leave
page 1 of their preferred search engine.
More simply put, giving you an advantage over your
competitors, quite literally.
"""
    logo_desription = """\
Logo creation for your Business of Event
Making a postive impression all starts with
what the customer sees when they land on your
webpage or walk up to see you in person
"""
    web_description = """\
We will create custom Web Applications to
simplify your Daily Tasks or save
you countless hours of auditing or tracking
for your Buisness or Event.
Can be for "in-house" use only
or used for Public Facing services also!
"""
    media_display = Path(
        data_path,
        'images/Services/Services1.png'
        )
    se_display = Path(
        data_path,
        'images/Services/TagLine1.png'
        )
    logo_display = Path(
        data_path,
        'images/Services/Services2.png'
        )
    wa_display = Path(
        data_path,
        'images/Services/Tagline2.png'
        )
    return {
        media_description: return_image_from_path(
            media_display
            ),
        seo_description: return_image_from_path(
            se_display
            ),
        logo_desription: return_image_from_path(
            logo_display
            ),
        web_description: return_image_from_path(
            wa_display
            ),
    }


def _services_page_func() -> None:
    services = _return_services_with_display()
    st.markdown(
        f"<h1 style='text-align: center; font-family: {FONT}; color:#EDEDED;'> \
        Services<h2>",
        unsafe_allow_html=True,
        )
    for service, view in services.items():
        col1, col2 = st.columns([1.5, 1])
        col1.markdown(
            f"<h2 style='text-align: center; font-family: {FONT};'> \
            <font size=6em>{service}</font></h2>",
            unsafe_allow_html=True,
            )
        col2.image(view)


def services_page_main():
    global FONT, FONT1
    import Contacts
    logo_path = str(
        Path(PurePath(__file__).parents[1],
             '.data', 'images', 'Logo', 'Social Outfit Logo.png'
             )
        )
    try:
        st.set_page_config(
            layout="wide",
            page_title='The Social Outfit - Services',
            page_icon=return_image_from_path(logo_path),
            )
    except st.errors.StreamlitAPIException:
        st.set_page_config(
            page_title='The Social Outfit - Services',
            page_icon=return_image_from_path(logo_path),
            )
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
