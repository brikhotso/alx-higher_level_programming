#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    add_prod = 0
    add_weight = 0

    for i in my_list:
        add_prod += i[0] * i[1]
        add_weight += i[1]

    return (add_prod / add_weight)
