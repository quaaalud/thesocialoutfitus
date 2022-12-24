# -*- coding: utf-8 -*-

import streamlit as st
from pathlib import Path

TEAM_IMG_DIR = Path(Path(__file__).parents[1], '.data', '.database', 'team')

@st.cache(suppress_st_warning=True)
def _get_team_images(team_img_dir=TEAM_IMG_DIR) -> dict:
    try:
        dirlist = [_file for _file in team_img_dir.iterdir()
                   if _file.is_file()
                   ]
        sorted_dirs = sorted(dirlist, key=lambda t: len(str(t)))
        file_names = [str(Path(_file.name).stem) for _file in sorted_dirs]
        team_dict = dict(zip(file_names, sorted_dirs))
        return team_dict
    except FileNotFoundError:
        team_img_dir.mkdir(parents=True)
        return dict()


if __name__ == '__main__':
    team_dict = _get_team_images()
    print(team_dict)
