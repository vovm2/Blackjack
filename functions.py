import random
from app import db

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


def new_deck():
    deck = []
    for suit in SUITS:
        for rank in RANKS:
            deck.append(str(suit+rank))
    random.shuffle(deck)
    return deck


def arr_to_str(arr):
    string = ','.join(arr)
    return string


def add(arr):
    value = 0
    flag = 0
    for i in arr:
        value += VALUES[i[1]]
        if VALUES[i[1]] == 1:
                flag = 1
    if value + 10 <= 21 and flag == 1:
        value += 10
    return value


def from_db(model):
    query = model.query.get(1)
    str_cards = query.cards
    return str_cards


def from_db2arr(model):
    deck = from_db(model).split(',')
    return deck


def to_db(model, deck):
    str_cards = arr_to_str(deck)
    query = model.query.get(1)
    query.cards = str_cards
    db.session.commit()
