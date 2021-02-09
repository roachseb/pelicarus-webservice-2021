from __future__ import print_function

import os.path
import pickle
from http import HTTPStatus

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build,Resource
from PelicarusDJWS.settings import API_CONFIGURATIONS, Struct
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://mail.google.com/',
          'https://www.googleapis.com/auth/gmail.modify',
          'https://www.googleapis.com/auth/gmail.compose',
          'https://www.googleapis.com/auth/gmail.send',
          'https://www.googleapis.com/auth/gmail.addons.current.action.compose']


class RESTAPI_HELPER():
    def __init__(self):
        self._headers = {'Content-Type': 'application/json'}
        self._baseURL = str(None)
        self._retryconfig = Retry(
            total=20,
            status_forcelist=(HTTPStatus.INTERNAL_SERVER_ERROR,
                              HTTPStatus.BAD_GATEWAY, HTTPStatus.GATEWAY_TIMEOUT))
        # Http Adapter Configuration (includes the retries)
        self._adapter = HTTPAdapter(max_retries=self._retryconfig)
        # Session Configuration
        self._session = Session()
        self._session.headers.update(self._headers)
        self._session.mount('http://', self._adapter)
        self._session.mount('https://', self._adapter)
        self._session.verify = False
        self._Configuration = API_CONFIGURATIONS




class GOOGLEAPI_HELPER():
    def __init__(self):
        """Shows basic usage of the Gmail API.
        Lists the user's Gmail labels.
        """
        self.creds = None
        self._Configuration = API_CONFIGURATIONS
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_config(self._Configuration.google,SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

        self.service:Resource = build('gmail', 'v1', credentials=self.creds)
