from django.apps import AppConfig
from requests.auth import HTTPBasicAuth
from collections import namedtuple
import unicodedata,os,json,requests


class HelloassoConfig(AppConfig):
    name = 'helloasso'

