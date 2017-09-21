#!/usr/bin/env python

import json
import os

#  print data['list'][2]['weather'][1]['main']


# def recursive(data, jsonpath, k, val, value):
#     for i,v in enumerate(data):
#         # dict - {} (not indexed)
#         if type(data) is dict:
#             # looking for a specific element supplied by the user
#             if v == jsonpath:
#                 return recursive(data[v], jsonpath, k, val, value)
#             # returning what the user wants - if it is a uniquey key
#             elif len(data) == 1 and t == value:
#                 return data[v]
#             # non-unique keys
#             else:
#                 for t in data.keys():
#                     if t == value:
#                         return data[t]
#         else: # assuming it is a list - [] (need an index)
#             for h,u in enumerate(data):
#                 # matching a specified key-value pair
#                 if data[h][k] == val:
#                     return recursive(data[h], jsonpath, k, val, value)

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

    with open("example2.json", "r") as json_file:
        data = json.load(json_file)

    search = "dt=1446940800,id=501"
    jsonpath = "list,weather,main"
    params_value = "Rain"

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

    for i,v in enumerate(data):
        if v == "list":
            data2 = data[v]
            for h,u in enumerate(data2):
                if data2[h]['dt'] == 1446940800:
                    data3 = data2[h]
                    for g,t in enumerate(data3):
                        if t == "weather":
                            data4 = data3[t]
                            for f,s in enumerate(data4):
                                if data4[f]['id'] == 501:
                                    print data4[f]['main']

if __name__ == "__main__":
    main()
