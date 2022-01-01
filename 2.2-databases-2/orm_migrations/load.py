import json
from pprint import pprint

with open("school.json", "r") as read_file:
    data = json.load(read_file)

pprint(data)
