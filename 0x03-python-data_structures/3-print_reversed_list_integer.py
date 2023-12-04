#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    pos = len(my_list) - 1
    for d in range(len(my_list)):
        if d < pos:
            tmp = my_list[d]
            my_list[d] = my_list[pos]
            my_list[pos] = tmp
            pos -= 1
