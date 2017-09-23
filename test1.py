#!/usr/bin/env python

import json
import os

def recursive(data, jsonpath, k, val, value):
    for i,v in enumerate(data):
        # dict - {} (not indexed)
        if type(data) is dict:
            # looking for a specific element supplied by the user
            if v == jsonpath:
                return recursive(data[v], jsonpath, k, val, value)
            # returning what the user wants - if it is a uniquey key
            elif len(data) == 1 and v == value:
                return data[v]
            # non-unique keys
            else:
                for t in data.keys():
                    if t == value:
                        return data[t]
        else: # assuming it is a list - [] (need an index)
            for h,u in enumerate(data):
                # matching a specified key-value pair
                if data[h][k] == val:
                    return recursive(data[h], jsonpath, k, val, value)

# def non_recursive(data, jsonpath, k, val, value):
#     for i,v in enumerate(data):
#         if v == jsonpath:
#             data2 = data[v]
#             if type(data2) is list:
#                 for h,u in enumerate(data2):
#                     if data2[h][k] == val:
#                         data3 = data2[h]
#                         if type(data3) is dict:
#                             for t in data3.keys():
#                                 if t == value:
#                                     return data3[t]

def main():

    with open("example1.json", "r") as json_file:
        data = json.load(json_file)

    jsonpath = "Students"
    search = "Major=Chemistry"
    value = "Name"

    k, val = search.split("=")

    print recursive(data, jsonpath, k, val, value)

if __name__ == "__main__":
    main()
