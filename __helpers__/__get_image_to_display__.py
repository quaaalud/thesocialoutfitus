# -*- coding: utf-8 -*-
"""
Created on Sun Nov  20 05:22:42 2022

@author: dludwinski
"""

from PIL import Image


def return_image_from_path(file_path: str) -> Image:
    """
    Take file path and returns PIL.Image for use in Streamlit App.

    Parameters
    ----------
    file_path : str

    Returns
    -------
    Image
        PIL.Image

    """
    return Image.open(file_path)


if __name__ == '__main__':
    from pathlib import Path, PurePath
    logo_path = str(
        Path(PurePath(__file__).parents[1],
             '.data/images/Logo/Social Outfit Logo.png')
    )
    img = return_image_from_path(logo_path)
    print(img)
