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


SERVICES = [
    'Build your Social Media Presence',
    'Search Engine Optimization',
    'Logo Creation',
    'Simple Web App Creation'
]


def services_page_main():
    global SERVICES
    logo_path = Path(
        PurePath(__file__).parents[1],
        PurePath('.data/images/Logo')
    )
    add_bg.add_bg_from_local(str(Path(logo_path, 'Social Outfit Logo.png')))
    st.header('Services Offered')
    for service in SERVICES:
        st.markdown(service)


if __name__ == '__main__':
    services_page_main()
