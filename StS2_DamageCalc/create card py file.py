import json
import reprlib  # noqa
import re

with open('cards.json', 'r', encoding='utf-8') as f:
    loaded = json.load(f)

# with open('cards.py', 'w', encoding='utf-8') as f_py:
#     f_py.write(loaded)

# print(reprlib.repr(loaded))

# キャラクター一覧
char_lst = set()
for card in loaded:
    char_lst.add(card['character'])

card_set = []

dct = {}
name = loaded[1]['name']
dct['name'] = name

cost = loaded[1]['cost']
dct['cost'] = int(cost)

damage = loaded[1]['description']
damage = re.findall(r'Deal (\d) ', damage)
dct['damage'] = int(damage[0])

print(dct)

# print(char_lst)

# キャラクター別に分ける
# for card in loaded:
#     temp
#     character = card['character']
#     if card['character'] == character

# 完成形
# []


# print(loaded[0]['character'])
