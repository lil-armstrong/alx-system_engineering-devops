#!/usr/bin/python3
"""Write to CSV file"""
import csv
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
            csv_file = "%s.csv" % (employee_id)
            user = requests.get(api + "users/%s" % (employee_id)).json()
            todos = requests.get(
                api + "todos", params={'userId': employee_id}).json()

            csv_rows = [[user.get('id'),
                         user.get('username'),
                         t.get('completed'),
                         t.get('title')] for t in todos]
            with open(csv_file, 'w', newline='') as f:
                csv_writer = csv.writer(f,
                                        quoting=csv.QUOTE_ALL)
                csv_writer.writerows(csv_rows)
        except Exception as err:
            print(err)
