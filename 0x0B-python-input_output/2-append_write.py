#!/usr/bin/python3
"""This is the module for appending"""


def append_write(filename="", text=""):
    """This is the method for appending to a file"""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        print(len(text))
