#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the top
10 hot posts for a given subreddit
"""

import requests


def top_ten(subreddit):
    """Queries the Reddit API for the top 10 posts
    for a given subreddit If the subreddit is invalid, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if posts:
            for post in posts[:10]:
                print(post.get('data', {}).get('title'))
            return
    print(None)
