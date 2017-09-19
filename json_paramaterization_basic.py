#!/usr/bin/env python

import json
import os

# jsonpath = []
# search = []
# value = ""
# k = []
# val = []
# def traverse(data,jsonpath,k,val,value):
#     for i,v in enumerate(data):
#         # good for capturing the base json
#         if v == jsonpath:
#             data2 = data[v]
#         elif type(data) is list:
#
#             data = data[u]
#             return traverse(data)


def non_recursive(data, jsonpath, k, val, value):
        for i,v in enumerate(data):
            if v == jsonpath:
                data2 = data[v]
                if type(data2) is list:
                    for j,u in enumerate(data2):
                        if data2[j][k] == val:
                            data3 = data2[j]
                            return data3[value]

def main():

    with open("example1.json", "r") as json_file:
        data = json.load(json_file)

    jsonpath = "Students"
    search = "Major=Chemistry"
    value = "Name"

    k, val = search.split("=")

    print non_recursive(data, jsonpath, k, val, value)


if __name__ == "__main__":
    main()