#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers or 0."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            try:
                data = response.json()
                subscribers = data['data']['subscribers']
                return subscribers
            except (ValueError, KeyError):
                return 0
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0
