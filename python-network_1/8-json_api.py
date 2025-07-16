#!/usr/bin/python3
"""Searches for a user by letter using a POST request"""

import requests
import sys

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': letter}

    try:
        response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
