# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:28:45 2022

@author: dludwinski
"""

import streamlit as st
import re

TSO_EMAIL = 'thesocialoutfits@gmail.com'


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


def contacts_page_main():
    global TSO_EMAIL
    st.header('Contact Us')
    st.subheader(f'Send us an email directly: {TSO_EMAIL}')
    st.write('Message us today to get the help you have been looking for')
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
            st.write(message_info)


if __name__ == '__main__':
    contacts_page_main()
