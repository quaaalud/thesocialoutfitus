# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 23:36:04 2022

@author: dludwinski
"""

import streamlit as st

SERVICES = [
    'Build your Social Media Presence',
    'Search Engine Optimization',
    'Logo Creation',
    'Simple Web App Creation'
]


def services_page_main():
    global SERVICES
    st.header('Services Offered')
    for service in SERVICES:
        st.markdown(service)


if __name__ == '__main__':
    services_page_main()
