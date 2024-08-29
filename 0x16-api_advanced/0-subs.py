#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""


import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers or 0."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        return 0
    return response.json().get("data").get("subscribers")
