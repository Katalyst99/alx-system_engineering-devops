#!/usr/bin/python3
"""
Python script that, for a given employee ID, returns information
about his/her TODO list progress extended to export data in the CSV format.
"""
import csv
import requests
import sys
if __name__ == "__main__":
    employE_ID = sys.argv[1]
    user_resp = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                             format(employE_ID)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(employE_ID)).json()

    uName = user_resp.get('username')
    with open('{}.csv'.format(employE_ID), "w", newline='') as csvf:
        csvw = csv.writer(csvf, quoting=csv.QUOTE_ALL)
        for t in todo:
            csvw.writerow([employE_ID, uName, t.get('completed'),
                           t.get('title')])
