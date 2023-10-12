#!/usr/bin/python3
"""
Sub-reddit keyword frequency module

Query the Reddit API for hot articles, 
Parse the title and 
Print a sorted count of given keywords (case-insensitive, delimited by spaces)
"""

import requests
from typing import List


def count_words(subreddit:str, word_list:List[str], log:dict|None = None,
                 data:dict | None = None) -> str:
    """
Recursive fn that return the sorted count of given keywords
Results are printed in descending order, by the count
Words are printed in lowercase
Results are based on the number of times a keyword appears, 
not titles it appears in
    """
    if len(word_list) < 1:
        entries = list(log.items())
        sorted_by_count = sorted(entries, key=lambda  x: (-x[1],x[0]))
        for entry in sorted_by_count:
            print(f"{entry[0]}: {entry[1]}")
        return
    
    url =f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
            "User-agent": "linux:0x016.api.advanced:v1.0.0"
    }

    freq = 0
    deduplicated = word_list

    if log is None:
        log = {}
        lowercased = [word.lower() for word in word_list]
        deduplicated = list(set(lowercased))

    keyword = deduplicated.pop()

    if data is None:
        res = requests.get(url, headers=headers,
                        allow_redirects=False)

        if res.status_code != 200:
            return None
            
        data = res.json().get("data").get("children")    

    for get_data in data:
        title:str = get_data.get("data").get("title")
        title = title.lower()

        for word in title.split():
            if word == keyword:
                freq += 1
    
    if freq:
        log[keyword] = freq
    return count_words(subreddit, deduplicated, log, data)
