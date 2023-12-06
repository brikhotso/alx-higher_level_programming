#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = list(a_dictionary.keys())

    for k in key_list:
        if value == a_dictionary.get(k):
            del a_dictionary[k]

    return (a_dictionary)
