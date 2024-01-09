#!/usr/bin/python3
""" contain function that reads a text file"""


def read_file(filename=""):
    """define function taht reads text file and print it to stdout"""
    with open(filename, encoding="UTF8") as file:
        content = file.read()
        print(content, end="")
