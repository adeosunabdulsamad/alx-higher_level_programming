#!/usr/bin/python3
"""This module for file handling"""


def read_file(filename=""):
    """This is the function for reading files"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
