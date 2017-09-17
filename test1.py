#!/usr/bin/env python

import json
import os

with open("example1.json", "r") as json_file:
    data = json.load(json_file)

    search = "Major=Chemistry"

    key, value = search.split("=")

    for c,i in enumerate(data['Students']):
        if i[key] == value:
            print data["Students"][c]["Name"]
