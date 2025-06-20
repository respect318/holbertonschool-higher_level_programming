#!/usr/bin/python3
def element_at(mylist,idx,element):
    if idx >= len(mylist):
        return mylist
    if idx <0:
        return mylist
    return mylist[idx]
