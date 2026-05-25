import json
items = json.load(open('seed/items.json'))
valid = [i for i in items if isinstance(i.get('amount'), (int, float)) and not isinstance(i.get('amount'), bool) and i.get('currency') == 'USD']
ids = sorted(i['id'] for i in valid)
s = sum(i['amount'] for i in valid)
with open('out/filtered_ids.json', 'w') as f:
    f.write(json.dumps(ids, separators=(',', ':')))
with open('out/sum.txt', 'w') as f:
    f.write(f'{s:.2f}')
