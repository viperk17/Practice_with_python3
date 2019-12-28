import json

with open('states.json') as f:
    data = json.load(f)  # loads load the string

for state in data['states']:
    # print(state['name'], state['abbreviation'])

    del state['area_codes']  # remove area codes

with open('new_states', 'w') as f:
    json.dump(data, f, indent=2)
