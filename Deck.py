import random
from Card import *


class Deck:
    def __init__(self):
        self.cardList = self._initialDeck()

    def _initialDeck(self):
        card_symbols = ["hearts", "clubs", "spades", "diamonds"]
        card_list = []
        for symbol in card_symbols:
            for i in range(2,15):
                card_list.append(Card(i, symbol))
        return card_list

    def addCard(self, newCard):
        if newCard not in self.cardList:
            self.cardList.append(newCard)

    def removeCard(self, newCard):
        if newCard in self.cardList:
            self.cardList.remove(newCard)

    def batchRemoveCards(self, batch):
        for card in batch:
            self.removeCard(card)
    
    def getTopCard(self):
        return self.cardList.pop(len(self.cardList) - 1)

    def shuffle(self, seed = None):
        if seed is None:
            random.shuffle(self.cardList)
        else:
            random.Random(seed).shuffle(self.cardList)

    def newDeck(self):
        return Deck()

    def __str__(self):
        return str(self.cardList)