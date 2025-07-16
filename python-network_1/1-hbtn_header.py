#!/usr/bin/python3
"""Fetches X-Request-Id header from a given URL"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        headers = response.headers
        print(headers.get("X-Request-Id"))
