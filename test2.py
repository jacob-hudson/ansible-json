#!/usr/bin/env python

import json
import os

with open("example1.json", "r") as json_file:
    data = json.load(json_file)

    for c,i in enumerate(data['Students']):
        if i['Major'] == "Chemistry":
            print data["Students"][c]["Name"]
