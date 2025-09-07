import json

# create Python object with type is dictionary
my_dict = {
    "name": "Huy Ta",
    "age": 20,
    "hobbies": ["eating", "sleeping", "coding"]
}

# Convert Python object dict to json string

json_string = json.dumps(my_dict) # json.dumps(my_dict)

# print(type(json_string))
# print(json_string)

# Convert json string to Python object dictionary
new_dict = json.loads(json_string)

# print(type(new_dict))
# print(new_dict)

# write to file
# assert new_dict == my_dict
# with open("output.json", "wt") as f:
#     json.dump(new_dict, f, indent=4)

# read from file json
# with open("output.json", "rt") as f:
#     my_content =  json.load(f)
#     print(my_content)
