from dataclasses import dataclass, asdict
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


# char: dict[char: str, cards: dict] 
# cards: dict[card_name: str, desc: dict]
# desc: dateclass(dict)[cost: int, damage: int]
# アクセス：card_list[The Silent][Strike].cost or .damage

card_list: dict[str, dict] = {}


@dataclass
class desc:
    cost: int | None
    damage: int


def add_card(card_list: dict, character: str, name: str, desc: desc):
    card_list.setdefault(character, {})[name] = desc


for card in loaded:
    character = card['character']
    name = card['name']
    cost = card['cost']
    if cost != 'X':
        cost = int(cost)
    else:
        cost = None
    damage = card['description']

    damage = re.findall(r'Deal (\d) ', damage)
    if damage == []:
        damage = 0
    else:
        damage = int(damage[0])

    add_card(card_list, character, name, desc(cost, damage))


# jsonファイルへの書き出し(表示確認用)
def default(o):
    if isinstance(o, desc):
        return asdict(o)
    raise TypeError(f'Object of type {type(o)} is not JSON serializable')


with open('card_list1.json', 'w', encoding='utf-8') as f:
    f.write('')
    json.dump(card_list, f, indent=2, default=default)

card_lst = {}
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
silent_cards = card_list['The Silent']

starter_deck_Silent = silent_cards['Strike'] * 5
starter_deck_Silent = silent_cards['Defend'] * 5
starter_deck_Silent = silent_cards['Survivor']
starter_deck_Silent = silent_cards['Neurtralize']


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
