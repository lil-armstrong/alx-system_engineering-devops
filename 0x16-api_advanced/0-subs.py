#!/usr/bin/python3
"""
Script queries the Reddit API and returns the number \
    of subscribers (not active users, total subscribers) for a given subreddit.
"""
import requests

if __name__ == "__main__":
    def get_subreddit_subscribers(subreddit):
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        # Set a custom User-Agent header
        headers = {'User-Agent': 'Custom User Agent'}

        try:
            response = requests.get(url, headers=headers)
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        except (requests.exceptions.RequestException, KeyError):
            return 0
