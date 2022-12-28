# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 20:04:45 2022

@author: dludwinski
"""


import os
# Gmail API utils
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.exceptions import RefreshError
from base64 import urlsafe_b64encode
from email.mime.text import MIMEText
from streamlit import cache

from dotenv import load_dotenv

load_dotenv()
email_user = os.getenv('PRIVATE_USERNAME')
email_pass = os.getenv('PRIVATE_PASSWORD')
client_id = os.getenv('PRIVATE_CLIENT_ID')
client_pass = os.getenv('PRIVATE_CLIENT_SECRET')


def get_creds() -> dict:
    SCOPES = ['https://mail.google.com/']
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except RefreshError:
                os.remove('token.json')
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json',
                    SCOPES
                    )
                creds = flow.run_local_server(port=0)
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json',
                SCOPES
                )
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


@cache
def build_message(destination:str, subject:str, body:str) -> dict:
    message = MIMEText(body)
    message['to'] = destination
    message['from'] = os.getenv('PRIVATE_USERNAME')
    message['subject'] = subject
    return {
        'raw': urlsafe_b64encode(message.as_bytes()).decode()
    }


def send_message(message:dict, creds=get_creds()) -> dict:
    with build('gmail', 'v1', credentials=creds) as s:
        s.users().messages().send(userId="me", body=message).execute()
    return message


def capture_and_send_email(dest=os.getenv('PRIVATE_USERNAME'),
                           subject=None,
                           body=None) -> dict:
    if subject or body:
        message = build_message(dest, subject, body)
        return send_message(message)


if __name__ == '__main__':
    destination = 'dludwins@outlook.com'
    subject = 'This is a test email'
    body = 'I am reallllly hoping that this works first try!'
    print(capture_and_send_email(dest=destination, subject=subject, body=body))
