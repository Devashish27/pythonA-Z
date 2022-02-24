import json

data = '{"var1":"tyron", "var2": 63}'
print(data)

parsed = json.loads(data)
# print(parsed['var1'])
print(type(parsed))


# Task1 - Json.load?

data2 = {

    "channel_name": "BreakingBad",
    "cars": ['bmw', 'mini-cooper', 'toyota-corolla', 'rangerover', 'mistubhishi-outlander'],
    "fridge": ('roti', 645),
    "isbad": False

}

jscomp = json.dumps(data2)
print(jscomp)

# Task = What is sort_keys parameter in dumps
