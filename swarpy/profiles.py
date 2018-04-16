#! python3
'''send requests to the /profiles endpoint of the swarfarm api'''
import os
import json
import click
import requests

SFAPI_URL = os.getenv('SFAPI_URL')


def get_profile(user_id):
  '''Get the profile information'''
  res = requests.get(f"{SFAPI_URL}{user_id}/")
  return res.content

