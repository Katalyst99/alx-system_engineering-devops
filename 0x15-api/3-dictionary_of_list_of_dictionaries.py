#!/usr/bin/python3
"""
Python script that, for a given employee ID, returns information
about his/her DO list progress extended to export data in the JSON format.
"""
import json
import requests
if __name__ == "__main__":
    usr = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    tjs = {}
    for u in usr:
        tlist = []
        u_Id = u.get('id')
        uName = u.get('username')
        todo = requests.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                    u_Id)).json()

        for t in todo:
            tlist.append({
                'username': uName,
                'task': t.get('title'),
                'completed': t.get('completed')})

            tjs[u_Id] = tlist
    with open('todo_all_employees.json', "w") as jf:
        json.dump(tjs, jf)
