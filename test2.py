#!/usr/bin/env python

import json
import os

with open("example2.json", "r") as json_file:
    data = json.load(json_file)

    search = "dt=1446940800,id=501"
    jsonpath = "list,weather,main"

    json_path = search.split(",")

    key = []
    value = []

    for i,jp in enumerate(json_path):
        k,v = jp.split("=")
        key.append(k)
        value.append(v)

    # print value[0]
    # if value[0].isdigit():
    #     value[0] = int(value[0])
    #     print value[0]

    for i,_ in enumerate(value):
        if value[i].isdigit():
            value[i] = int(value[i])

# print data['list'][2]['weather'][1]['main']
    for c,i in enumerate(data['list']):
        if i[key[0]] == value[0]:
            for b,i in enumerate(data['list'][c]['weather']):
                if i[key[1]] == value[1]:
                    print data['list'][c]['weather'][b]['main']
