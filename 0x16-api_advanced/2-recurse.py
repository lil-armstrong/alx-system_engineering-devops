#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""


from typing import List
import requests


def recurse(
        subreddit,
        hot_list=None,
        after=None,
        limit: int = 25) -> List[str]:
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
        "limit": limit,
        "after": after
    }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        return None

    data = res.json().get("data")
    children = data.get("children")
    after = data.get("after")

    for get_data in children:
        title: str = get_data.get("data").get("title")
        titles.append(title)

    if after is not None:
        # Recursive call with updated 'after' parameter to fetch the next page
        return recurse(subreddit, titles, after, limit - len(titles))

    return titles
