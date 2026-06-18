from dataclasses import dataclass
import json
import reprlib  # noqa
import re

with open('cards.json', 'r', encoding='utf-8') as f:
    loaded = json.load(f)

# with open('cards.py', 'w', encoding='utf-8') as f_py:
#     f_py.write(loaded)

# print(reprlib.repr(loaded))

# キャラクター一覧
# char_lst = set()
# for card in loaded:
#     char_lst.add(card['character'])

# 旧カードリスト作成（キャラ分け無し）
# card_lst = {}
# for card in loaded:
#     dct_inner = {}
#     name = card['name']
#     card_lst[name] = dct_inner

#     cost = card['cost']
#     if cost != 'X':
#         dct_inner['cost'] = int(cost)
#     else:
#         dct_inner['cost'] = cost

#     damage = card['description']
#     damage = re.findall(r'Deal (\d) ', damage)
#     if damage == []:
#         dct_inner['damage'] = 0
#     else:
#         dct_inner['damage'] = int(damage[0])

card_lst = {}

@dataclass
class Char:
    card_name: str
    desc: dict

    def add_card(self, card_name, desc):
        self.card_name[] = desc

for card in loaded:
    dct_inner = {}
    name = card['name']
    card_lst[name] = dct_inner

    cost = card['cost']
    if cost != 'X':
        dct_inner['cost'] = int(cost)
    else:
        dct_inner['cost'] = cost

    damage = card['description']
    damage = re.findall(r'Deal (\d) ', damage)
    if damage == []:
        dct_inner['damage'] = 0
    else:
        dct_inner['damage'] = int(damage[0])

# jsonファイルへの書き出し(表示確認用)
with open('card_list.json', 'w', encoding='utf-8') as f:
    f.write('')
    json.dump(card_lst, f, indent=2)

# スターターデッキ作成
starter_deck_Silent = []
for _ in range(5):
    starter_deck_Silent.append(card_lst['Strike'])
    starter_deck_Silent.append(card_lst['Defend'])
starter_deck_Silent.append(card_lst['Survivor'])
starter_deck_Silent.append(card_lst['Neutralize'])


print(starter_deck_Silent)

# print(char_lst)
# キャラクター別に分ける
# for card in loaded:
#     temp
#     character = card['character']
#     if card['character'] == character

# 完成形
# []


# print(loaded[0]['character'])
