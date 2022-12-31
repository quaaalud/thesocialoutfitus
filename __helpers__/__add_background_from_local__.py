# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 13:33:31 2022

@author: dludwinski
"""

import base64
from streamlit import markdown


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-position: top center;
        background-size: 100% 100%;
        display: flex;
        border: 2px solid;
        color: white;
        background-repeat: no-repeat;
        filter: brightness(100%)
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


if __name__ == '__main__':
    pass
