#!/bin/env python3

import requests
import urllib.request

headers = {'user-agent': 'Mosaic Netscape 0.9'}
url = 'http://www.pornhub.com'

response = requests.get(url, headers=headers, timeout=5)

if response.ok:
   print ("Tits is accessible!")
else:
   print ("Please change your ISP")
