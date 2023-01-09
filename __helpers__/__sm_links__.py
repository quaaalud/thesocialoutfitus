#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 22:16:29 2022

@author: dale
"""


import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

import streamlit as st
from __get_image_to_display__ import _img_to_bytes

def _get_all_sm_logos() -> list:
    sm_logo_dir = Path(
        Path(__file__).parents[1],
        '.data',
        '.database',
        'sm_logos'
    )
    return [file for file in sm_logo_dir.iterdir() if file.is_file()]


def _return_sm_links_dict() -> dict:
    return {
        'Facebook': 'https://www.facebook.com/thesocialoutfitus',
        'Instagram': 'https://www.instagram.com/thesocialoutfitus',
        'Twitter': 'https://twitter.com/socialoutfitUS',
    }

@st.cache(allow_output_mutation=True)
def _get_sm_logo_and_link() -> dict:
    sm_logos_list = _get_all_sm_logos()
    logos_dict = {}
    for logo in sm_logos_list:
        temp_key = Path(logo).stem
        logos_dict[logo] = _return_sm_links_dict().get(temp_key)
    return logos_dict


def sm_logo_link_to_html(web_path: str, 
                         img_path: str) -> str:
    try:
        img_html = f"""
        <p style="text-align:center;"><u>
        <a href='{web_path}'>
        <img src='data:image/png;base64,{_img_to_bytes(img_path)}'>
        </a>
        </p>
        """
    except:
        img_html = f"""
        <p style="text-align:center;"><u>
        <a href='{web_path}'>
        <img src='data:image/jpg;base64,{_img_to_bytes(img_path)}'>
        </a>
        </p>
        """
    return img_html


def _display_sm_links() -> None:
    logo_link_dict = _get_sm_logo_and_link()
    st.markdown('<br><p> </p>', unsafe_allow_html=True)
    em1, col1, em2, col2, em3, col3, em4 = st.columns(
        [3, 0.5, 0.1, 0.5, 0.1, 0.5, 3],
        gap='small',
        )
    for sm_logo, sm_link in logo_link_dict.items():
        if 'facebook' in sm_link:
            col1.markdown(sm_logo_link_to_html(sm_link, sm_logo),
                          unsafe_allow_html=True,
                          )
        if 'instagram' in sm_link:
            col2.markdown(sm_logo_link_to_html(sm_link, sm_logo),
                          unsafe_allow_html=True,
                          )
        if 'twitter' in sm_link:
            col3.markdown(sm_logo_link_to_html(sm_link, sm_logo),
                          unsafe_allow_html=True,
                          )
    with st.container():
        visit_txt = """
        <p style='text-align:center; color:gray;'>
        <b>Vist our social media pages and connect with us today</b>
        </p>"""
        st.markdown(visit_txt, unsafe_allow_html=True)
            
            
if __name__ == '__main__':
    print(_get_sm_logo_and_link())
