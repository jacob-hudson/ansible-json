#!/usr/bin/env python

import json
import os

# def traverse(data,search,value):
#     for i,v in enumerate(data):
#         if v == result:
#             if value == r:
#                 return value:
#         elif type(data) is list:
#
#             data = data[u]
#             return traverse(data)

def main():

    with open("example1.json", "r") as json_file:
        data = json.load(json_file)

    jsonpath = "Students"
    search = "Major=Chemistry"
    value = "Name"

    k, val = search.split("=")

    for i,v in enumerate(data):
        if v == jsonpath:
            data2 = data[v]


    if type(data2) is list:
        for j,u in enumerate(data2):
            if data2[j][k] == val:
                data3 = data2[j]
                print data3[value]


if __name__ == "__main__":
    main()
