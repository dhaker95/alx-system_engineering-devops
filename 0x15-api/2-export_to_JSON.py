#!/usr/bin/python3
"""
Shows the complete tasks done by a specific employee ID
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Get the todo list
    url = 'https://jsonplaceholder.typicode.com/todos'
    params = (('userId', sys.argv[1]),)
    t = requests.get(url, params=params)

    # Get the user info
    url = 'https://jsonplaceholder.typicode.com/users'
    params = (('id', sys.argv[1]),)
    u = requests.get(url, params=params)

    # Convert to json
    todos = t.json()
    user = u.json()

    tasks = []
    for task in todos:
        task_dict = {}
        task_dict["task"] = task['title']
        task_dict["completed"] = task['completed']
        task_dict["username"] = user[0]['username']
        tasks.append(task_dict)
    jsonobj = {}
    jsonobj[sys.argv[1]] = tasks
    with open("{}.json".format(sys.argv[1]), 'w') as jsonfile:
        json.dump(jsonobj, jsonfile)
