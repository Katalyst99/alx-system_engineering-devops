#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Katalyst:v1.0.0'}
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code != 200:
        return 0
    output = resp.json().get('data')
    subs = output.get('subscribers')
    return subs
