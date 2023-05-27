#!/usr/bin/python3
'''Get information about a given employee TODO list'''
import sys

import requests

if __name__ == "__main__":
    argv = sys.argv[1:]

    if len(argv) != 1:
        print("Usage: %s <ID>" % (sys.argv[0]))
    else:
        try:
            employee_id = argv[0]
            api = "https://jsonplaceholder.typicode.com/"
            user = requests.get(api + "users/%s" % (employee_id)).json()
            todos = requests.get(
                api + "todos", params={'userId': employee_id}).json()
            completed = [todo.get("title")
                         for todo in todos if todo.get("completed") is True]
            print("Employee %s is done with tasks (%d/%d)" %
                  (user.get('name'), len(completed), len(todos)))
            [print("\t " + item) for item in completed]
        except Exception as err:
            print(err)
