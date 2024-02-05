#!/usr/bin/python3
"""
Script that, for a given employee ID, returns information about their TODO
list progress exported as a csv file
"""

import csv
import requests
from sys import argv

def main():
    """
    Query name and tasks of employee.
    """
    if len(argv) >= 2 and argv[1].isdigit():
        id = argv[1]

    url_todos = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    url_id = f"https://jsonplaceholder.typicode.com/users/{id}"

    response = requests.get(url_id)

        if response.status_code != 200:
            print(f"Error:username not found")
            exit()

        data = response.json()
        EMPLOYEE_NAME = data["username"]

        response = requests.get(url_todos)

        if response.status_code != 200:
            print(f"Error:username not found")
            exit()

        todos = response.json()

        all_tasks = [todo["title"] for todo in todos]
        status_task = [todo["completed"] for todo in todos]
        employee_todos = []

        for index in range(0, len(all_tasks)):
            record = [str(id), EMPLOYEE_NAME, str(
                status_task[index]), all_tasks[index]]

            employee_todos.append(record)

        name_file_csv = f"{id}.csv"

        with open(name_file_csv, mode="w", newline="") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerows(employee_todos)

        else:
            print("Please enter an existing user id")

    if __name__ == "__main__":
        main()
