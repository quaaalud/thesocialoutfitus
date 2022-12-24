# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:28:45 2022

@author: dludwinski
"""

import streamlit as st
import re
from pathlib import Path, PurePath
import sys
sys.path.append(str(Path(PurePath(__file__).parents[1], '__helpers__')))
sys.path.append(str(Path(PurePath(__file__).parents[1], '.data')))
import __send_message_to_email__ as send_email
import __get_team_members__ as get_team
from __get_image_to_display__ import (
    return_image_from_path,
    return_image_from_path_and_resize_large,
    )


FONT = 'Nanum Gothic'
FONT1 = 'Papyrus'
        

def get_contact_info(name: str,
                     email: str,
                     phone='',
                     message='') -> dict:
    valid_email = _confirm_email_is_valid(email)
    if valid_email:
        return {
            'name': _check_name_is_ascii(name),
            'email': email,
            'phone': _check_phone_numbers(phone),
            'message': _check_message_is_ascii(message),
        }
    else:
        return None


def _check_name_is_ascii(name: str) -> str:
    if name.isascii():
        return name.capitalize()
    else:
        return ''


def _confirm_email_is_valid(email_str: str) -> str:
    email_regex = re.compile(
        r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])"
    )
    if re.fullmatch(email_regex, email_str):
        return email_str
    else:
        return ''


def _check_phone_numbers(phone: str) -> str:
    remchars = ['(', ')', '-', '+', ' ']
    for char in phone:
        if char in remchars:
            phone = phone.replace(char, '')
    if phone.isnumeric():
        return phone
    else:
        return ''


def _check_message_is_ascii(message='') -> str:
    if message.isascii():
        return message
    else:
        return ''


def _concat_all_dict_values(dictionary: dict):
    all_vals = [str(val) for val in dictionary.values()]
    return '\n\n'.join(all_vals)


@st.cache(suppress_st_warning=True)
def _get_current_team_members():
    return get_team._get_team_images()


def _display_current_team_members():
    team_dict = _get_current_team_members()
    with st.container():
        col1, col2, col3 = st.columns(3, gap='small')
        col1.markdown(
            """
            <p style='text-align: center'>
            <u>Dale Ludwinski</u><br>
            <small>Operations & Analytics
            </small></p>
            """,
            unsafe_allow_html=True,
        )
        col2.markdown(
            """
            <p style='text-align: center'>
            <u>Aaron Childs</u><br>
            <small>Founder & Creative Director
            </small></p>
            """,
            unsafe_allow_html=True,
        )
        col3.markdown(
            """
                    <p style='text-align: center'>
                    <u>Jack Trippi</u><br>
                    <small>Recruitment & Brand Coordinator
                    </small></p>
                    """,
            unsafe_allow_html=True,
        )
        for key, val in team_dict.items():
            if 'dale' in str(key).lower():
                with st.container():
                    col1.image(return_image_from_path_and_resize_large(val),
                               caption=key,
                               use_column_width='always',
                               )
            elif 'aaron' in str(key).lower():
                with st.container():
                    col2.image(return_image_from_path_and_resize_large(val),
                               caption=key,
                               use_column_width='always',
                               )
            elif 'jack' in str(key).lower():
                with st.container():
                    col3.image(return_image_from_path_and_resize_large(val),
                               caption=key,
                               use_column_width='always',
                               )


def _email_form_func() -> None:
    name = st.text_input('Your Name:', max_chars=30)
    email = st.text_input('Email:', max_chars=50)
    phone = st.text_input('Phone:', max_chars=20)
    question = st.text_area('How can we help you:',
                            height=40,
                            max_chars=500,
                            )
    message_info = get_contact_info(name,
                                    email,
                                    phone=phone,
                                    message=question
                                    )
    if message_info:
        if st.button('Submit'):
            send_email.capture_and_send_email(
                dest='thesocialoutfitus@gmail.com',
                subject=email,
                body=_concat_all_dict_values(message_info),
                )
            st.markdown(
                f"<p style='text-align: center; font-family: {FONT};'> \
                Message Sent</p>",
                unsafe_allow_html=True
                )


def contacts_page_main():
    """

    Streamlit GUI with Contact Form and Current Team Member information.

    Messages are sent to thesocialoutfitus@gmail.com and all email addresses
    are captured and added to the contacts.db file for later use

    Returns
    -------
    None.

    """
    logo_dir = Path(PurePath(__file__).parents[1],
                    '.data', 'images', 'Logo'
                    )
    logo_path = str(Path(logo_dir, 'The Social Outfit.png'))
    st.set_page_config(
        layout='wide',
        page_title='The Social Outfit - Contact Us',
        page_icon=return_image_from_path(logo_path),
        menu_items=None,
        initial_sidebar_state='collapsed',
        )
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    global FONT, FONT1
    TSO_EMAIL = 'thesocialoutfitus@gmail.com'
    main_logo = str(Path(logo_dir, 'Social Outfit Logo All White Slim.png'))
    col1, col2, col3 = st.columns([2.5, 5, 2.5])
    col2.image(return_image_from_path(main_logo),
               use_column_width=True,
               )
    st.header('Contact Us')
    st.subheader(f'Send us an email directly: {TSO_EMAIL}')
    _email_form_func()
    _display_current_team_members()


if __name__ == '__main__':
    contacts_page_main()
