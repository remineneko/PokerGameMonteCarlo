from Card import *
from itertools import combinations


class CommunityCard:
    def __init__(self):
        self.card_list = []
        self.comm_card_amt_limit = 5
    
    def addCard(self, card:Card):
        if card not in self.card_list:
            self.card_list.append(card)

    def allThreeCardsSet(self):
        # Essentially generates all combinations of three cards amongst the community cards.
        return list(combinations(self.card_list, 3))

    def clearBoard(self):
        self.card_list = []

    def comCardLen(self):
        return len(self.card_list)  

    def __str__(self):
        return "     ".join([str(card) for card in self.card_list])

    def __contains__(self, obj):
        if obj in self.card_list:
            return True
        else:
            return False

    def __iter__(self):
        return iter(self.card_list)