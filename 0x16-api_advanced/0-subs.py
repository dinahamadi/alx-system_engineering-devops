#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of
    subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent 1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 404:
            return 0
        elif response.status_code == 200:
            data = response.json().get("data")
            if data and data.get("subscribers") is not None:
                return data["subscribers"]
            else:
                return 0
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0
