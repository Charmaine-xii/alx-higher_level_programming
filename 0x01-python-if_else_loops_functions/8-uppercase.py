#!/usr/bin/python3
def uppercase(string):
    for char in string:
        upper_char = chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char
        print("{}".format(upper_char), end="")
    print("")

