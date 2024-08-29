#!/usr/bin/python3
"""Queries the Reddit API recursively to get all
hot articles' titles"""

import requests


def recurse(subreddit, hot_list=None):
    """Recursively queries Reddit API to get a list
    of hot article titles for a given subreddit."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            after = data.get('after', None)
            if posts:
                for post in posts:
                    hot_list.append(post.get('data', {}).get('title'))
            if after:
                next_url = url + "?after=" + after
                return recurse(subreddit, hot_list)
            else:
                return hot_list
        else:
            return None
    except requests.exceptions.RequestException:
        return None
