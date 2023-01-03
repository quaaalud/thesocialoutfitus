# -*- coding: utf-8 -*-


import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

import streamlit as st

HOME_PAGE = 'http://thesocialoutfitus.com'

# @st.cache(allow_output_mutation=True)
def _list_all_pages() -> dict:
    global HOME_PAGE
    pages_dir = Path(
        Path(__file__).parents[1],
        'pages'
        )
    pages_dict = {'Home': HOME_PAGE}
    for page in pages_dir.iterdir():
        if page.is_file():
            pages_dict[page.stem] = f'{HOME_PAGE}/{page.stem}'
    return pages_dict
    

def _return_pages_links_html(page_name:str, web_path:str) -> str:
    return f"""
    <h4 style="text-align:center; color:gray"><u>
    <a href='{web_path}' target='_self'>
    {page_name.title()}
    </u>
    </h4>
    """
    
def _convert_pages_dict_to_html(pages_dict: dict) -> list:
    return [
        _return_pages_links_html(page_name, web_path) for 
        page_name, web_path in pages_dict.items()
        ]

def _display_pages_links():
    st.markdown('<p><br></p>', unsafe_allow_html=True)
    pages_dict = _list_all_pages()
    pages_html = _convert_pages_dict_to_html(pages_dict)
    e0, col0, e1, col1, e2, col2, e3, col3, e4 = st.columns(
        [1, 0.5, 0.2, 0.5, 0.2, 0.5, 0.2, 0.5, 1],
        gap='small'
        )
    for i, page in enumerate(pages_html):
        if i == 0:
            col0.markdown(page, unsafe_allow_html=True)
        if i == 1:
            col1.markdown(page, unsafe_allow_html=True)
        if i == 2:
            col2.markdown(page, unsafe_allow_html=True)
        if i == 3:
            col3.markdown(page, unsafe_allow_html=True)
    st.markdown("""
                <p style='text-align:center; color:gray;'> <br><br>
                © 2023 All Rights Reserved
                </p>
                """, 
                unsafe_allow_html=True
                )


if __name__ == '__main__':
    pass