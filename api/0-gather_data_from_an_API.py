#!/usr/bin/python3
"""
Script that using.
https://jsonplaceholder.typicode.com/
"""

import requests
from sys import argv

if __name__ == "__main__":
    """ code not executed when imported """
    emp = argv[1]
    url_request = "https://jsonplaceholder.typicode.com/users/{}".format(emp)
    url = requests.get(url_request)
    emp_name = url.json().get('name')
    todos = requests.get("{}/todos".format(url_request)).json()
    done_tasks = 0
    total = 0
    todo_list = []
    for task in todos:
        total += 1
        if task.get('completed'):
            done_tasks += 1
            todo_list.append(task.get("title"))
    print("Employee {} is done with tasks:({}/{}):".format(
            emp_name, done_tasks, total))
    for task in todo_list:
        print("\t {}".format(task))
