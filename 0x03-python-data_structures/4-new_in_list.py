#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return None
    l = my_list.copy()
    l[idx] = element
    return l
