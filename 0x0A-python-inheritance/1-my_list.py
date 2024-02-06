#!/usr/bin/python3
"""This module  is a child class of the class List"""


class MyList(list):
    """MyList is a child class of the class List"""

    def __init__(self):
        """This is the constructor function of the class"""

        super().__init__()

    def print_sorted(self):
        """This is a function to print ou the list"""
        print(sorted(self))
