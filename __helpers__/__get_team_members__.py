# -*- coding: utf-8 -*-

import streamlit as st
from pathlib import Path

TEAM_IMG_DIR = Path(Path(__file__).parents[1], '.data', '.database', 'team')

@st.cache(suppress_st_warning=True)
def _get_team_images(team_img_dir=TEAM_IMG_DIR) -> dict:
    try:
        dirlist = team_img_dir.iterdir()
    except FileNotFoundError:
        team_img_dir.mkdir(parents=True)
    dirlist = [_file for _file in team_img_dir.iterdir()
               if _file.is_file()
               ]
    sorted_dirs = sorted(dirlist, key=lambda t: t.lstat().st_mtime)
    file_names = [_file.name.split('.')[0] for _file in sorted_dirs]
    return dict(zip(file_names, sorted_dirs))
    
    
if __name__ == '__main__':
    ...
    