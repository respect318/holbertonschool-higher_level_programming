#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    copy_list = my_list[:]
    if idx < 0 or idx >= len(copy_list):
        return copy_list
    copy_list[idx] = element
    return copy_list
