#!/usr/bin/python3
"""
Usings API for extract information false.
"""

from sys import argv
import json
import requests

def main():
    """
    Query name and tasks of employee.
    """

    all_employees = {}

    for id in range(1, 11):
        """
        Use API URL to get user tasks and information
        """

        url_id = f"https://jsonplaceholder.typicode.com/users/{id}"
        url_todos = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

        response = requests.get(url_id)

        if response.status_code != 200:
            print(f"Error:username not found. Please enter an existing user id")
            exit()

        data = response.json()
        EMPLOYEE_NAME = data["username"]

        response = requests.get(url_todos)

        if response.status_code != 200:
            print(f"Error:username not found. Please enter an existing user id")
            exit()

        todos = response.json()
        list_todos = []
        dict_todos = {}

        all_tasks = [todo["title"] for todo in todos]
        status_task = [todo["completed"] for todo in todos]

        for index in range(0, len(all_tasks)):
            dict_todos = {
                "username": EMPLOYEE_NAME,
                "task": all_tasks[index],
                "completed": status_task[index]
            }

            list_todos.append(dict_todos)

            employee_todos = {str(id): list_todos}

        all_employees.update(employee_todos)

        name_file_json = "todo_all_employees.json"

        with open(name_file_json, mode="w", newline='') as f:
            json.dump(all_employees, f, indent=4)


if __name__ == "__main__":
    main()
