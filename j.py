import json
my_json_data = """[
    1,
    {
        "2": 3,
        "4": [
            "5",
            "6",
            "7"
        ]
    },
    8,
    9
]"""

def recursive_iter(obj):
    if isinstance(obj, dict):
        for item in obj.values():
            yield from recursive_iter(item)
    elif any(isinstance(obj, t) for t in (list, tuple)):
        for item in obj:
            yield from recursive_iter(item)
    else:
        yield obj

data = json.loads(my_json_data)
for item in recursive_iter(data):
    print(item)
