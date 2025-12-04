# serialization
import json
person = {"name": "john", "age": 30, "city": "New York", "hasChildren": False, "titles":["engineer", "programmer"]}

print(person.get('titles'))
print(person.items())

personJSON = json.dumps(person, indent=4, sort_keys=True)
# print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4, sort_keys=True)

# DESERIALIZING
with open('person.json', 'r') as file:
    data = json.load(file)
    print(type(data))
    print(person['age'])