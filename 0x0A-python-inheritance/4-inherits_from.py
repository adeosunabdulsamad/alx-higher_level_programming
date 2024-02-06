#!/usr/bin/python3
"""This is the module for subclass"""


def inherits_from(obj, a_class):
    """This is the function for subclass instnace"""
    b_class = type(obj)
    if b_class == a_class:
        return False
    else:
        return issubclass(b_class, a_class)
