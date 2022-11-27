# -*- coding: utf-8 -*-


import os
import requests
from dotenv import load_dotenv
from pathlib import Path, PurePath

load_dotenv(str(Path(PurePath(__file__).parents[1], '.env')))


def get_business_list(business_type: str,
                      state: str,
                      api_key=os.getenv('XRAPID_KEY'),
                      page=1) -> dict:
    url = "https://local-business-data.p.rapidapi.com/search"

    querystring = {
        'ypkeyword': business_type,
        "yplocation": state.lower(),
        "yppage": int(page),
        }
    headers = {
        "content-type": 'application/json',
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": 'yellow-page-us.p.rapidapi.com'
    }

    return requests.request("GET", url, params=querystring, headers=headers)


if __name__ == '__main__':
    response = get_business_list('dispensary', 'missouri')
    print(response.content)
    save_path = 'C:/Users/dludwinski/Desktop/All Missouri Dispensaries.txt'
    with open(save_path, 'wb') as file:
        file.write(response.content)
