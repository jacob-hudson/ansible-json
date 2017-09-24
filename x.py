#!/usr/bin/env python

import json
import os

# jsonpath = []
# search = []
# value = ""
# k = []
# val = []


# def recursive(data, jsonpath, k, val, value):
#     for i,v in enumerate(data):
#         if v == jsonpath:
#             recursive(data[v], jsonpath, k, val, value)
#         elif type(data) is list:
#             for j,u in enumerate(data):
#                 if data[j][k] == val:
#                     recursive(data[j], jsonpath, k, val, value)
#         elif data.keys() == value:
#             return data[value]

def non_recursive(data, jsonpath, k, val, value):
        for i,v in enumerate(data):
            if v == jsonpath:
                data = data[v]
                if type(data) is list:
                    for j,u in enumerate(data):
                        if data[j]['Major'] == val:
                            data = data[j]
                            if data.keys() == value:
                                return data[value]

def main():

    with open("example1.json", "r") as json_file:
        data = json.load(json_file)

    jsonpath = "Students"
    search = "Major=Chemistry"
    value = "Name"

    k, val = search.split("=")

#    print non_recursive(data, jsonpath, k, val, value)

    for i,v in enumerate(data):
        if v == jsonpath:
            data2 = data[v]
            if type(data3) is list:
                for j,u in enumerate(data):
                    if data[j][k] == val:
                        data = data[j]
                        if data.keys() == value:
                            return data[value]


if __name__ == "__main__":
    main()
