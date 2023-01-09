# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:35:34 2022

@author: dludwinski
"""


from pathlib import PurePath, Path
from os import getcwd


def get_directory_path(file_type: str) -> PurePath:
    return Path(__PATHS__()._paths_dict()[file_type])


class __PATHS__:
    """
    Class for managing all Paths used within the website/application

    """

    def __init__(self):
        self._PAGES_DIR = PurePath(getcwd(), 'pages')
        self._DATA_DIR = PurePath(getcwd(), '.data')
        self._DB_PATH = PurePath(self._DATA_DIR, '.database/contacts.db')
        self.animations = PurePath(self._DATA_DIR, 'animations')
        self.images = PurePath(self._DATA_DIR, 'images')
        self.music = PurePath(self._DATA_DIR, 'music')
        self.videos = PurePath(self._DATA_DIR, 'videos')
        self.websites_apps = PurePath(self._DATA_DIR, 'websites_apps')

    def _paths_dict(self):
        return self.__dict__

    def return_portfolio_directories(self):
        return {
            ftype: str(dirpath) for ftype, dirpath in
            self._paths_dict().items() if not
            ftype.startswith('_') and not
            ftype.startswith('.')

        }


if __name__ == '__main__':
    paths = __PATHS__()
    for k, v in paths.return_portfolio_directories().items():
        print(k)
        print(v)
        print()
