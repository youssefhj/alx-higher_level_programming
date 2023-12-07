#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    my_list = set(my_list)
    for n in my_list:
        res += n
        
    return res
