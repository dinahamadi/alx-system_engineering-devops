#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the top
10 hot posts for a given subreddit
"""

import requests


def top_ten(subreddit):
    """Queries the Reddit API for the top 10 posts
    for a given subreddit. If the subreddit is invalid,
    prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 404:
            print(None)
        elif response.status_code == 200:
            try:
                data = response.json()
                posts = data.get('data', {}).get('children', [])
                if posts:
                    for post in posts[:10]:
                        print(post.get('data', {}).get('title'))
                else:
                    print(None)
            except ValueError:
                print(None)
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)
