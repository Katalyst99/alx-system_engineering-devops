#!/usr/bin/python3
"""
A function that queries the Reddit API ,
and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Returns the first 10 hot posts listed"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Google chrome:v127.0.6533.90'}
    params = {'limit': 10}
    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)
    if resp.status_code != 200:
        print(None)
        return

    data = resp.json().get('data')
    if data is None:
        print(None)
        return

    hotList = data.get('children')
    if hotList is None:
        print(None)
        return
    else:
        for post in hotList:
            title = post.get('data').get('title')
            print(title)
