import json

with open("outputs/output.json") as json_file:
    nfa = json.load(json_file)

print(nfa['objective'])