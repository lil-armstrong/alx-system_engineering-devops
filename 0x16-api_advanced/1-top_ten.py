#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API"""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-agent": "linux:0x016.api.advanced:v1.0.0"
    }
    params = {
        "limit": 10
    }
    res = requests.get(URL, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 200:
        for get_data in res.json().get("data").get("children"):
            title = get_data.get("data").get("title")
            print(title)
    else:
        print(None)
