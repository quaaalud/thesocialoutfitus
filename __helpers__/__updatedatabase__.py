# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 19:32:04 2022

@author: dludwinski
"""


from pathlib import Path, PurePath
import os
import sys
sys.path.append(str(Path(__file__).parent))
sys.path.append(str(Path(PurePath(__file__).parents[1], '.data')))

import pandas as pd
import sqlalchemy as sa
import __pathconstants__ as pth
import __createdatabase__ as cdb


def return_db_path():
    if Path(pth.__PATHS__()._DB_PATH).exists():
        return f'sqlite:///{str(Path(pth.__PATHS__()._DB_PATH))}'
    elif (Path(__file__).parents[1] == Path(os.getcwd())):
        return f'\
sqlite:///{cdb.create_db("contacts", str(Path(pth.__PATHS__()._DB_PATH)))}'
    else:
        str_path = 'C:/Users/dludwinski/dale_working_folder/thesocialoutfitus/.data/.database/contacts.db'
        return f'sqlite:///{Path(str_path)}'


def capture_user_info(message_dict: dict) -> None:
    engine = sa.create_engine(return_db_path())
    with engine.connect() as e:
        contacts_db = pd.read_sql_table('contacts', e)
        new_contact = cdb.get_contact_info_for_db(message_dict)
        print(new_contact)
        updated_db = contacts_db.merge(
            new_contact,
            how='outer',
            on=['Email', 'Name', 'Phone']
            ).drop_duplicates(
                subset=['Email'],
                keep='last',
                ignore_index=True
                )
        print(updated_db)


if __name__ == '__main__':
    message_dict = {'email': 'dludwins@outlook.com',
                    'name': 'Dale',
                    'phone': '314-650-5443',
                    }
    print(cdb.get_contact_info_for_db(message_dict))
    capture_user_info(message_dict)
