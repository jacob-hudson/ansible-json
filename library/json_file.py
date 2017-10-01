#!/usr/bin/env python

from ansible.module_utils.basic import *
import json
import os

DOCUMENTATION = ''' docs '''
EXAMPLES = ''' examples '''

# global variables
jnum = 0
kvnum = 0

def traverse_path(data, json_path, key, value, params_value):
    # uses variables from the global namespace
    global jnum
    global kvnum
    for i,v in enumerate(data):
        # dict - {} (not indexed)
        if type(data) is dict:
            # looking for a specific element supplied by the user
            if jnum < len(json_path):
                if v == json_path[jnum]:
                    jnum += 1
                    return traverse_path(data[v], json_path, key, value, params_value)
            # returning what the user wants - if it is a uniquey key
            elif len(data) == 1 and v == params_value[0]:
                return False, False, data[v]
            # non-unique keys
            elif len(data) > 1 and data.has_key(params_value[0]):
                for t in data.keys():
                    if t == params_value[0]:
                        if not isinstance(data[t], dict):
                            return False, False, data[t]
            else:
                pass # do nothing
        else: # assuming it is a list - [] (need an index)
            for h,u in enumerate(data):
                # matching a specified key-value pair
                if data[h][key[kvnum]] == value[kvnum]:
                    if kvnum < len(key):
                        kvnum += 1
                        return traverse_path(data[h], json_path, key, value, params_value)
                    else:
                        return False, False, data[h][params_value[0]]

def open_json(params):

    with open(params['filepath'], "r") as json_file:
        data = json.load(json_file)

    json_path = params['jsonpath'].split(",")
    search_path  = params['search'].split(",")
    params_value = params['value'].split('=')

    key = []
    value = []

    for i,sp in enumerate(search_path):
        k,v = sp.split("=")
        key.append(k)
        value.append(v)

    for i,_ in enumerate(value):
        if value[i].isdigit():
            value[i] = int(value[i])

    is_error, has_changed, value = traverse_path(data, json_path, key, value, params_value)
    return is_error, has_changed, value

def main():

    fields = {
        "filepath": {"required": True, "type": "str"},
        "jsonpath": {"required": True, "type": "str"},
        "search": {"required": False, "type": "str"},
        "value": {"required": True, "type": "str"},
    }

    module = AnsibleModule(argument_spec=fields)

    is_error, has_changed, result = open_json(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Something bad happened", meta=result)

if __name__ == "__main__":
    main()
