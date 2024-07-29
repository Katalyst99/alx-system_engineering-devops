#!/usr/bin/python3
"""
Python script that, for a given employee ID, returns information
about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    employE_ID = sys.argv[1]
    user_resp = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                             format(employE_ID)).json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(employE_ID)).json()

    tasksDone = [tasks.get('title') for tasks in todo if tasks
                 .get('completed') is True]
    emp = user_resp.get('name')
    T_tasks = len(todo)
    NDt = len(tasksDone)
    print("Employee {} is done with tasks({}/{}):".format(emp, NDt, T_tasks))
    for tasks in tasksDone:
        print('\t {}'.format(tasks))
