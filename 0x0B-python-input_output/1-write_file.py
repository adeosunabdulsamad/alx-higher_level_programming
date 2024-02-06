#!/usr/bin/python3
"""This module for file handling"""


def write_file(filename="", text=""):
    """This is the function for writing to files"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        print(len(str(text)))
