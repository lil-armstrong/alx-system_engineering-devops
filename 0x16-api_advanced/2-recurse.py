#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""


import requests
from typing import List


def recurse(
        subreddit,
        hot_list: List[str] | None = None,
        after: str | None = None,
        count: int = 0) -> List[str]:
    """
    Query the sub-reddit
    return a list of titles of all hot articles
    """
    if hot_list is None:
        titles = []
    else:
        titles = hot_list[:]

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        "User-agent": "linux:0x016.api.advanced:v1.0.0"
    }
    params = {
        "limit": 100,
        "after": after,
        "count": count
    }

    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        return None

    data = res.json().get("data")
    children = data.get("children")
    after = data.get("after")
    count = data.get('dist')

    for get_data in children:
        title: str = get_data.get("data").get("title")
        titles.append(title)

    if after is not None:
        return recurse(subreddit, titles, after, count)

    return titles
