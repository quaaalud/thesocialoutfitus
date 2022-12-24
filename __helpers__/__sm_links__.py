#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 22:16:29 2022

@author: dale
"""


import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from __get_image_to_display__ import return_image_from_path_and_resize_small

def _get_all_sm_logos():
    sm_logo_dir = Path(
        Path(__file__).parents[1],
        '.data',
        '.database',
        'sm_logos'
    )
    return [file for file in sm_logo_dir.iterdir() if file.is_file()]


def _return_sm_links_dict():
    return {
        'Facebook': 'https://www.facebook.com/thesocialoutfitus',
        'Instagram': 'https://www.instagram.com/thesocialoutfitus',
        'Twitter': 'https://twitter.com/thesocialoutfitus',
    }

def _get_sm_logo_and_link():
    sm_logos_list = _get_all_sm_logos()
    logos_dict = {}
    for logo in sm_logos_list:
        temp_key = Path(logo).stem
        logos_dict[logo] = _return_sm_links_dict().get(temp_key)
    return logos_dict
        
        
    

if __name__ == '__main__':
    print(_get_sm_logo_and_link())
