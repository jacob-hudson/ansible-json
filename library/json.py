#!/usr/bin/env python

from ansible.module_utils.basic import *
import json
import os

DOCUMENTATION = ''' docs '''

EXAMPLES = ''' examples '''

def traverse_path():

    for c,i in params['jsonpath']:
        if i[-1] == params['value']
            return c

def open_json(params):

    with open(params['filepath'], "r") as json_file:
        data = json.load(json_file)

    value = traverse_path(params, data)
    return false, faluse, data['jsonpath'][value]['value']

def main():

    fields = {
        "filepath": {"required": True, "type": "str"},
        "jsonpath": {"required": True, "type": "str"},
        "value": {"required": True, "type": "str"},
    }

    is_error, has_changed, result = open_json(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Something bad happened", meta=result)

if __name__ == "__main__":
    main()
