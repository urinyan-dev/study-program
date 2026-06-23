from dataclasses import dataclass, asdict
import json
import reprlib  # noqa
import re
import random as rd

with open('cards.json', 'r', encoding='utf-8') as f:
    loaded = json.load(f)

# char: dict[char: str, cards: dict]
# cards: dict[card_name: str, desc: dict]
# desc: dateclass(dict)[cost: int, damage: int]
# アクセス：card_list[The Silent][Strike].cost or .damage

card_list: dict[str, list] = {}


class CardList(list):
    @property
    def names(self):
        return [card.name for card in self]

    @property
    def costs(self):
        return [card.cost for card in self]

    @property
    def damages(self):
        return [card.damage for card in self]


@dataclass
class desc:
    name: str
    cost: int | None
    damage: int


def add_card(all_card: dict, character: str, desc: desc):
    all_card.setdefault(character, []).append(desc)


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

    add_card(card_list, character, desc(name, cost, damage))


# dataclassを正しくjson形式で書き出すための処理
def default(o):
    if isinstance(o, desc):
        return asdict(o)
    raise TypeError(f'Object of type {type(o)} is not JSON serializable')


# jsonファイルへの書き出し(表示確認用)
with open('card_list.json', 'w', encoding='utf-8') as f:
    f.write('')
    json.dump(card_list, f, indent=2, default=default)

# サイレントのカードリストを表示させてみる
silent_cards = CardList(card_list['The Silent'])
# print(reprlib.repr(silent_cards))


# スターターデッキ作成
def add_card_to_deck(card_name: str, deck: CardList, list: CardList, count: int = 1):  # noqa
    for card in list:
        if card.name == card_name:
            for _ in range(count):
                deck.append(card)
            return


starter_deck_Silent = CardList([])
add_card_to_deck('Strike', starter_deck_Silent, silent_cards, 5)
add_card_to_deck('Defend', starter_deck_Silent, silent_cards, 5)
add_card_to_deck('Survivor', starter_deck_Silent, silent_cards, 1)
add_card_to_deck('Neutralize', starter_deck_Silent, silent_cards, 1)
# print(starter_deck_Silent)


# ターンを進める処理
# drawはシャッフルされた状態で渡す
def turn_going(draw: CardList, discard: CardList, count: int = 1):

    print(f'draw={draw.names}')
    hand = CardList([])

    for _ in range(5):
        hand.append(draw.pop())

    # print(f'hand={hand.names}')
    # print(f'draw={draw.names}')
    # print(f'discard={discard.names}')

    # 手札のカードを使用優先順位で並び替える
    hand.sort(key=lambda card: (-card.cost, card.damage))
    print(f'hand={hand.names}')

    # カードを使用する
    energy = 3
    damage = 0
    while energy > 0:
        card = hand.pop()
        if card is None:
            print('Error')
        print(f'{card=}')
        energy -= card.cost
        damage += card.damage
        discard.append(card)

    print(f'{damage=}')
    print(f'hand={hand.names}')
    return damage


draw = CardList(starter_deck_Silent.copy())
rd.shuffle(draw)
discard = CardList([])
turn_going(draw, discard, 1)

# 1ターンの平均ダメージを出してみる
total = 0
n = 10000
for _ in range(n):
    draw = CardList(starter_deck_Silent.copy())
    rd.shuffle(draw)
    discard = CardList([])
    total += turn_going(draw, discard, 1)
average = total / n
print(f'{average=}')


# ダメージ計算
def damage_calc_with_turn(deck: list, turn: int):
    pass
