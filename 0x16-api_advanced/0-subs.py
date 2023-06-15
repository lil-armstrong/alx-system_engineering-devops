#!/usr/bin/python3
"""

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
