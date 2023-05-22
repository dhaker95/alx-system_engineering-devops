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
    t = requests.get(url)

    # Get the user info
    url = 'https://jsonplaceholder.typicode.com/users'
    u = requests.get(url)

    # Convert to json
    todos = t.json()
    users = u.json()

    user_dict = {}

    for user in users:
        username = user['username']
        user_infos = []

        for task in todos:
            if task['userId'] == user['id']:
                dict_info = {}
                dict_info['username'] = username
                dict_info['task'] = task['title']
                dict_info['completed'] = task['completed']
                user_infos.append(dict_info)
        user_dict[user['id']] = user_infos

    with open("todo_all_employees.json", 'w') as f:
        json.dump(user_dict, f)
