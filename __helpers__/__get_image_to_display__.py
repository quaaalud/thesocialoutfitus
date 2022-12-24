# -*- coding: utf-8 -*-
"""
Created on Sun Nov  20 05:22:42 2022

@author: dludwinski
"""

import base64
from PIL import Image
from pathlib import Path


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


def return_image_from_path_and_resize_small(file_path: str) -> Image:
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
    img = Image.open(file_path)
    img = img.resize((25, 25))
    return img


def return_image_from_path_and_resize(file_path: str) -> Image:
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
    img = Image.open(file_path)
    img = img.resize((500, 500))
    return img

def return_image_from_path_and_resize_medium(file_path: str) -> Image:
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
    img = Image.open(file_path)
    img = img.resize((800, 800))
    return img


def return_image_from_path_and_resize_large(file_path: str) -> Image:
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
    img = Image.open(file_path)
    img = img.resize((2000, 2000))
    return img


def _img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


if __name__ == '__main__':
    from pathlib import PurePath
    logo_path = str(
        Path(PurePath(__file__).parents[1],
             '.data/images/Logo/Social Outfit Logo.png')
    )
    img = return_image_from_path(logo_path)
    print(img)
