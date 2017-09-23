#!/usr/bin/env python

import json
import os

#  print data['list'][2]['weather'][1]['main']


def recursive(data, json_path, key, value, params_value):
    for i,v in enumerate(data):
        # dict - {} (not indexed)
        if type(data) is dict:
            # looking for a specific element supplied by the user
            if v == json_path:
                return recursive(data, json_path[v], key, value, params_value)
            # returning what the user wants - if it is a uniquey key
        elif len(data) == 1 and t == params_value:
                return data[v]
            # non-unique keys
            else:
                for t in data.keys():
                    if t == params_value:
                        return data[t]
        else: # assuming it is a list - [] (need an index)
            for h,u in enumerate(data):
                # matching a specified key-value pair
                if data[h][key] == value:
                    return recursive(data, json_path[v], key, value, params_value)

def non_recursive(data, json_path, key, value, params_value):
    for i,v in enumerate(data):
        if v == json_path[0]:
            data2 = data[v]
            for h,u in enumerate(data2):
                if data2[h][key[0]] == value[0]:
                    data3 = data2[h]
                    for g,t in enumerate(data3):
                        if t == json_path[1]:
                            data4 = data3[t]
                            for f,s in enumerate(data4):
                                if data4[f][key[1]] == value[1]:
                                    return data4[f][params_value]

def main():

    with open("example2.json", "r") as json_file:
        data = json.load(json_file)

    search = "dt=1446940800,id=501"
    jsonpath = "list,weather"
    params_value = "main"

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

    print non_recursive(data, json_path, key, value, params_value)


if __name__ == "__main__":
    main()
