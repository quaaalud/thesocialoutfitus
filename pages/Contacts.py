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
import __add_background_from_local__ as add_bg
import __send_message_to_email__ as send_email


TSO_EMAIL = 'thesocialoutfits@gmail.com'  # Uncomment this line when live
# TSO_EMAIL = 'dludwins@outlook.com'


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


def _display_current_team_members():
    team_dir = Path(
        PurePath(__file__).parents[1],
        '.data',
        '.database',
        '.team'
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
    try:
        st.set_page_config(
            layout="wide",
            page_title='The Social Outfit - Contact Us',
            )
    except:
        pass
    global TSO_EMAIL
    logo_path = Path(
        PurePath(__file__).parents[1],
        PurePath('.data/images/Logo')
    )
    # add_bg.add_bg_from_local(str(Path(logo_path,
    #                                  'Social Outfit Logo.png'))
    #                         )
    st.header('Contact Us')
    st.subheader(f'Send us an email directly: {TSO_EMAIL}')
    st.write('Message us today to get the help you have been looking for!')
    try:
        my_expander = st.expander(label='Click Here to Message Us')
        with my_expander:
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
                        dest=TSO_EMAIL,
                        subject=email,
                        body=_concat_all_dict_values(message_info),
                        )
                    st.write('Message Sent!')
    except:
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
                    dest=TSO_EMAIL,
                    subject=email,
                    body=_concat_all_dict_values(message_info),
                    )
                st.write('Message Sent!')


if __name__ == '__main__':
    contacts_page_main()
