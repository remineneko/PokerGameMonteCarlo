import os
from Card import Card

def _get_file_data(path):
    if os.path.isfile(path) and os.path.splitext(path)[-1] == '.txt':
       with open(path, 'r') as f:
           return f.readlines()
    else:
        raise ValueError("Please double check your path.")

def _convert_to_cards(data, datatype):
    suit_start_mapping = {"H":"Hearts","S":"Spades","D":"Diamonds","C":"Clubs"}
    rank_mapping = {"A": 14, "K":13, "Q": 12, "J": 11}
    all_cards = datatype()
    for info in data:
        suit, rank = info.split(", ")
        final_suit = suit_start_mapping[suit[0]]
        try:
            if int(rank) <= 10:
                final_rank = int(rank)
            else:
                final_rank = rank_mapping[rank[0]]
        except ValueError:
            final_rank = rank_mapping[rank[0]]
        all_cards.addCard(Card(final_rank, final_suit)) # will only work when and only when addCard exists and have same signature across all classes used.
    return all_cards

def convert(path, datatype):
    return _convert_to_cards(_get_file_data(path), datatype)
        