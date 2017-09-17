#!/usr/bin/env python

import json
import os

with open("example2.json", "r") as json_file:
    data = json.load(json_file)

# print data['list'][2]['weather'][1]['main']
    for c,i in enumerate(data['list']):
        if i['dt'] == 1446940800:
            for b,i in enumerate(data['list'][c]['weather']):
                if i['id'] == 501:
                    print data['list'][c]['weather'][b]['main']
