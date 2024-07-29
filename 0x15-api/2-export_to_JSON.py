#!/usr/bin/python3
"""
Python script that, for a given employee ID, returns information
about his/her DO list progress extended to export data in the JSON format.
"""
import json
import requests
import sys
if __name__ == "__main__":
    employE_ID = sys.argv[1]
    user_resp = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                             format(employE_ID)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(employE_ID)).json()

    uName = user_resp.get('username')
    tlist = []
    for t in todo:
        tlist.append({
            'task': t.get('title'),
            'completed': t.get('completed'),
            'username': uName})

    tjs = {}
    tjs[employE_ID] = tlist
    with open('{}.json'.format(employE_ID), "w") as jf:
        json.dump(tjs, jf)
