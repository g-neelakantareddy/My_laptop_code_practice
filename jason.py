import json

with open('states.json') as f:
    data = json.load(f)

neela = []
for state in data['states']:
    del state['code']

with open('new_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)