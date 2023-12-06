#!/usr/python3
def complex_delete(a_dictionary, value):
    for k in list(a_dictionary.keys()):
        if value == a_dictionary.get(k):
            del a_dictionary[k]

    return (a_dictionary)
