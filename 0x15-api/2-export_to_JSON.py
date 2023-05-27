#!/usr/bin/python3
"""Format and save response to JSON"""
import json
import requests
import sys


if __name__ == "__main__":
    argv = sys.argv[1:]

    if len(argv) != 1:
        print("Usage: %s <ID>" % (sys.argv[0]))
    else:
        try:
            employee_id = argv[0]
            api = "https://jsonplaceholder.typicode.com/"
            file_name = "%s.json" % (employee_id)
            user = requests.get(api + "users/%s" % (employee_id)).json()
            todos = requests.get(
                api + "todos", params={'userId': employee_id}).json()

            rows = [{"task": t.get('title'),
                     "completed": t.get('completed'),
                     "username": user.get('username'),
                     }
                    for t in todos]

            with open(file_name, 'w') as f:
                json.dump({user.get('id'): rows}, f)
        except Exception as err:
            print(err)
