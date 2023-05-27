#!/usr/bin/python3
"""Format and save response to JSON"""
import json
import requests


if __name__ == "__main__":

    try:
        api = "https://jsonplaceholder.typicode.com/"
        file_name = "%s.json" % ("todo_all_employees")
        users = requests.get(api + "users").json()
        records = {}
        for user in users:
            todos = requests.get(
                api + "todos", params={'userId': user.get('id')}).json()
            rows = [{"task": t.get('title'),
                     "completed": t.get('completed'),
                     "username": user.get('username'),
                     }
                    for t in todos]
            records[user.get('id')] = rows

        with open(file_name, 'w') as f:
            json.dump(records, f)
    except Exception as err:
        print(err)
