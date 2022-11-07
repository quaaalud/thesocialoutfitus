# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:16:22 2022

@author: dludwinski
"""

import streamlit as st
from pathlib import PurePath, Path
import sys
sys.path.append(str(Path(PurePath(__file__).parent, '.data')))
sys.path.append(str(Path(PurePath(__file__).parent, 'pages')))


def main():
    import Contacts
    import Portfolio
    st.header('Welcome to The Social Outfit')
    with st.container():
        st.subheader(
            "Saving you time so your business can do what it's best at!"
        )


def _get_db_connection():
    import __pathconstants__
    import __createdatabase__


if __name__ == '__main__':
    main()
