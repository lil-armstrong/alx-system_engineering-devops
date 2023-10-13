#!/usr/bin/python3
"""
Verifies that a student's function is recursive
"""
import sys
import traceback

from io import StringIO


def check_recursion():
    """
    Verifies that a student's code is using recursion.
    """
    sys.settrace(trace_calls)
    trace = StringIO()
    stderr = sys.stderr
    sys.stderr = trace

    recurse('hello')
    sys.stderr = stderr

    if len(trace.getvalue()) > 0:
        print("function is recursive", end="")
    else:
        print("function is not recursive", end="")


def trace_calls(frame, event, arg):
    if event != 'call':  # We only want function calls!
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name != 'recurse':  # We only want function calls of THIS function
        return
    func_line_no = frame.f_lineno
    func_filename = co.co_filename
    caller = frame.f_back
    caller_line_no = caller.f_lineno
    caller_filename = caller.f_code.co_filename
    if 'main' in caller_filename:  # Ignore any calls made in main
        return
    sys.stderr.write('Call to {} on line {} of {} from line {} of {}\n'
                     .format(func_name,
                             func_line_no,
                             func_filename,
                             caller_line_no,
                             caller_filename))


if __name__ == "__main__":
    recurse = __import__('2-recurse').recurse
    check_recursion()
