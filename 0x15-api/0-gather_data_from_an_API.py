#!/usr/bin/python3
"""
Shows the complete tasks done by a specific employee ID
"""

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

    done = []
    for task in todos:
        if task['completed'] is True:
            done.append(task)

    print("Employee {} is done with tasks({}/{}):".
          format(user[0]['name'], len(done), len(todos)))
    if len(done) > 0:
        for task in done:
            print("\t {}".format(task['title']))
