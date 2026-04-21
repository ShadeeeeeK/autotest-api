import json

data = {
    'name': 'Sergey',
    'age': 25,
    'qwe': None
}

with open('json_example.json', 'w', encoding='utf-8') as js:
    json.dump(data, js, ensure_ascii=False, indent=2)