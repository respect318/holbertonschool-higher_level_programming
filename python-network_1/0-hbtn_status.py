#!/usr/bin/python3
import urllib.request

url = 'https://intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode('utf-8'))
except Exception as e:
    print(f"Error fetching the URL: {e}")
