#!/bin/env python3

import requests
import urllib.request

headers = {'user-agent': 'Mosaic Netscape 0.9'}
url = 'http://www.pornhub.com'

response = requests.get(url, headers=headers, timeout=5)

if response.ok:
   print ("tits is accessible!")
else:
   print ("please change your ISP")
