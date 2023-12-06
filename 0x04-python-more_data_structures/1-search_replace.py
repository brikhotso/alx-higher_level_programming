#!/usr/bin/phython3

def search_replace(my_list, search, replace):
    orig_list = my_list.copy()

    for i in range(len(orig_list)):
        if orig_list[i] == search:
            orig_list[i] = replace

    return orig_list
