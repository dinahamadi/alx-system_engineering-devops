#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers or 0."""
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        return 0
    return response.json().get("data").get("subscribers")
