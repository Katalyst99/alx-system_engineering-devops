#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Katalyst'}
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        output = data.get('data')
        subs = output.get('subscribers')
        return subs
    else:
        return 0
