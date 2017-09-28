#!/usr/bin/env python

import json
import os

# global variables
jnum = 0
kvnum = 0

def recursive(data, json_path, key, value, params_value):
    # uses variables from the global namespace
    global jnum
    global kvnum
    for i,v in enumerate(data):
        # dict - {} (not indexed)
        if type(data) is dict:
            # looking for a specific element supplied by the user
            if jnum < len(json_path):
                if v == json_path[jnum]:
                    jnum = jnum + 1
                    return recursive(data[v], json_path, key, value, params_value)
            # returning what the user wants - if it is a uniquey key
            elif len(data) == 1 and v == params_value:
                return data[v]
            # non-unique keys
            elif len(data) > 1 and data.has_key(params_value):
                for t in data.keys():
                    if t == params_value:
                        if not isinstance(data[t], dict):
                            return data[t]
            else:
                pass
        else: # assuming it is a list - [] (need an index)
            for h,u in enumerate(data):
                # matching a specified key-value pair
                if data[h][key[kvnum]] == value[kvnum]:
                    if kvnum < len(key):
                        kvnum += 1
                        return recursive(data[h], json_path, key, value, params_value)
                    else:
                        return data[h][params_value]

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
    params_value = "Name"

    json_path = jsonpath.split(",")
    search_path  = search.split(",")

    key = []
    value = []

    for i,sp in enumerate(search_path):
        k,v = sp.split("=")
        key.append(k)
        value.append(v)

    for i,_ in enumerate(value):
        if value[i].isdigit():
            value[i] = int(value[i])

    print recursive(data, json_path, key, value, params_value)

if __name__ == "__main__":
    main()
