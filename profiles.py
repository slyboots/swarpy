#! python3
'''send requests to the /profiles endpoint of the swarfarm api'''

import json
import requests

SFAPI_URL = 'https://swarfarm.com/api/v2/profiles/'
def get_profile(user_id):
  '''Get the profile information'''
  res = requests.get(f"{SFAPI_URL}{user_id}/")
  return res.content

