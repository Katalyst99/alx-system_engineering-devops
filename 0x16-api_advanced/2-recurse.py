#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list,
containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[]):
    """Returns a list containing the titles of all hot articles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Google chrome:v127.0.6533.90'}
    params = {'limit': 100}
    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)
    if resp.status_code != 200:
        return None

    data = resp.json().get('data')
    if data is None:
        return None

    hotArt = data.get('children',)
    for art in hotArt:
        title = art.get('data',).get('title')
        if title:
            hot_list.append(title)

    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list)
    return hot_list
