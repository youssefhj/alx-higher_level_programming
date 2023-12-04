#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for tab in matrix:
        for i in range(len(tab)):
            print('{:d}'.format(tab[i]), end='\n' if i is len(tab) - 1 else " ")
