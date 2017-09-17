#!/usr/bin/env python

import json
import os

with open("example2.json", "r") as json_file:
    data = json.load(json_file)

    search = "dt=1446940800,id=501"
    jsonpath = "list,weather,main"

    json_path = jsonpath.split(",")


    jp1 = data[json_path[0]]


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

#  print data['list'][2]['weather'][1]['main']
    for c,i in enumerate(jp1):
        if i[key[0]] == value[0]:
            jp2 = data[json_path[0]][c][json_path[1]]
            for b,i in enumerate(jp2):
                if i[key[1]] == value[1]:
                    print data['list'][c]['weather'][b]['main']
