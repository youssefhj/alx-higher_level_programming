#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    listd = []
    for i in my_list:
        if (i % 2) == 0:
            listd.append(True)
        else:
            listd.append(False)

    return listd
