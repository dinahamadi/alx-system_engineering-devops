#!/usr/bin/python3
"""Queries the Reddit API and counts the occurrences of keywords
in hot article titles."""


from collections import defaultdict
import re
import requests


def count_words(subreddit, word_list, hot_list=None, after=None):
    """Recursively queries Reddit API to count keyword occurrences
    in hot article titles."""

    if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"

    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            after = data.get('after', None)
            if posts:
                for post in posts:
                    hot_list.append(post.get('data', {}).get('title', ''))
            if after:
                return count_words(subreddit, word_list, hot_list, after)
            else:
                return count_keyword_occurrences(hot_list, word_list)
        else:
            return None
    except requests.exceptions.RequestException:
        return None


def count_keyword_occurrences(hot_list, word_list):
    """Counts occurrences of keywords in hot_list and prints sorted results."""
    keyword_count = defaultdict(int)
    word_patterns = {
        word.lower(): re.compile(
            r'\b' + re.escape(word.lower()) + r'\b', re.IGNORECASE
        )
        for word in word_list
    }
    for title in hot_list:
        for keyword, pattern in word_patterns.items():
            keyword_count[keyword] += len(pattern.findall(title))

    sorted_keywords = sorted(
        keyword_count.items(), key=lambda x: (-x[1], x[0])
    )

    for keyword, count in sorted_keywords:
        if count > 0:
            print(f"{keyword}: {count}")
