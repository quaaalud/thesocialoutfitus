# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:31:42 2022

@author: dludwinski
"""


from pathlib import Path, PurePath
import sys

sys.path.append(str(Path(PurePath(__file__).parents[1], '.data')))

import __pathconstants__ as pth
import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ContactsData(Base):
    __tablename__ = 'contacts'

    Email = Column(String, primary_key=True)
    Name = Column(String)
    Phone = Column(Integer)


def _check_if_db_exists(db_path=pth.__PATHS__()._DB_PATH) -> Path:
    db_path = Path(db_path)
    if db_path.exists():
        return db_path
    else:
        dirpath = db_path.parents[0]
        if not _check_if_db_exists(db_path=dirpath):
            from os import mkdir
            mkdir(str(dirpath))
        return None


def _capture_email_phone_or_name(message_dict: dict,
                                 capture_str: str) -> dict:
    return message_dict.get(capture_str)


def get_contact_info_for_db(message_dict: dict) -> pd.DataFrame:
    contact_info = pd.DataFrame()
    email = _capture_email_phone_or_name(message_dict, 'email')
    contact_info.insert(
        0,
        'Email',
        email
        )
    print(email)
    contact_info.insert(
        1,
        'Name',
        str(_capture_email_phone_or_name(message_dict, 'name'))
        )
    contact_info.insert(
        2,
        'Phone',
        str(_capture_email_phone_or_name(message_dict, 'phone'))
        )
    return contact_info.fillna('None')


def create_db(
        table_name: str,
        db_path=pth.__PATHS__()._DB_PATH) -> bool:

    if not _check_if_db_exists(db_path=db_path):
        dbengine = create_engine(f'sqlite:///{db_path}')
        Base.metadata.tables[table_name].create(dbengine)
        dbengine.dispose()
    return _check_if_db_exists(db_path=db_path)




if __name__ == '__main__':
    print(create_db('contacts'))
