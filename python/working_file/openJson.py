import json
 
import json

data = {
    'subject': ['a', 'b'],
    'taskName': ['c', 'd'],
    'day': [1, 3],
    'month': [8, 9],
    'year': [2022, 2022]
}
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)