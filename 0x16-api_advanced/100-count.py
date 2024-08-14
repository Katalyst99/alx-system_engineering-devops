#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses
the title of all hot articles, and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after="", counts=None):
    """Prints a sorted count of given keywords"""
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Google chrome:v127.0.6533.90'}
    params = {'limit': 100}
    resp = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)
    if resp.status_code != 200:
        return

    data = resp.json().get('data')
    if not data:
        return

    hotArt = data.get('children',)
    for art in hotArt:
        title = art.get('data',).get('title').lower()

        for word in word_list:
            count = title.split().count(word.lower())
            if count > 0:
                counts[word.lower()] = counts.get(word.lower(), 0) + count

    after = data.get('after')
    if after:
        return count_words(subreddit, word_list, after, counts)
    else:
        s_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in s_counts:
            print("{}: {}".format(word, count))
