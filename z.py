#!/usr/bin/python

d = {'key_1': 'value_1',
     'key_2': {'key_21': [(2100, 2101), (2110, 2111)],
           'key_22': ['l1', 'l2'],
           'key_23': {'key_231': 'v'},
           'key_24': {'key_241': 502,
                      'key_242': [(5, 0), (7, 0)],
                      'key_243': {'key_2431': [0, 0],
                                  'key_2432': 504,
                                  'key_2433': [(11451, 0), (11452, 0)]},
                      'key_244': {'key_2441': ['ll1', 'll2']}}}}

def search_it(nested, target):
    found = []
    for key, value in nested.iteritems():
        if key == target:
            found.append(value)
        elif isinstance(value, dict):
            found.extend(search_it(value, target))
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    found.extend(search_it(item, target))
        else:
            if key == target:
                found.append(value)
    return found

keys = [ 'key_242', 'key_243', 'key_242', 'key_244', 'key_1' ]

for key in keys:
    f = search_it(d, key)
    print 'Key: %s, value: %s' % (key, f[0])
