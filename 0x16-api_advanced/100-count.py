#!/usr/bin/python3
"""
Sub-reddit keyword frequency module

Query the Reddit API for hot articles,
Parse the title and
Print a sorted count of given keywords (case-insensitive, delimited by spaces)
"""

import requests
from typing import List


def count_words(subreddit: str, word_list: List[str], log: dict | None = None,
                after: str | None = None, count: int | None = None) -> str:
    """
Recursive fn that return the sorted count of given keywords
Results are printed in descending order, by the count
Words are printed in lowercase
Results are based on the number of times a keyword appears,
not titles it appears in
    """
    if log is not None and after is None:
        entries = list(log.items())
        sorted_by_count = sorted(entries, key=lambda x: (-x[1], x[0]))
        for entry in sorted_by_count:
            print(f"{entry[0]}: {entry[1]}")
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-agent": "linux:0x016.api.advanced:v1.0.0"
    }
    params = {
        "limit": 100,
        "after": after,
        "count": count
    }
    deduplicated = word_list

    if log is None:
        log = {}
        lowercased = [word.lower() for word in word_list]
        deduplicated = list(set(lowercased))

    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    result = res.json().get("data")
    children = result.get("children")
    after = result.get('after')
    count = result.get('dist')

    for data in children:
        title: str = data.get("data").get("title")
        title = title.lower()
        words = title.split()

        for keyword in deduplicated:
            for word in words:
                if word == keyword:
                    log[keyword] = log.get(keyword, 0) + 1

    
    return count_words(subreddit, deduplicated, log, after, count)
