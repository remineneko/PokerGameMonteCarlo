from Card import Card
from CommunityCard import CommunityCard
from copy import deepcopy


class PokerHand:
    def __init__(self):
        self.hand = []
        self.hand_limit = 2

    def addCard(self, card:Card):
        if card not in self.hand:
            self.hand.append(card)

    def clearHand(self):
        self.hand = []

    def evaluate(self, communitySet: CommunityCard):
        '''
        Evaluates the entire hand with the entire set of community cards.
        This evaluation takes 2 cards from the player's hand and 5 cards
            from the community set into consideration.
        Hence, evaluate should only be called when all 5 community cards have been
            shown on the board.
        :param communitySet: the set of community cards
        :return:
        '''
        value_list = []
        all_hands = []
        for cardSet in communitySet.allThreeCardsSet():
            comCardList = deepcopy(cardSet)
            hand_copy = deepcopy(self.hand)
            hand_copy.extend(comCardList)
            hand_suits = list(dict.fromkeys([card.suit for card in hand_copy]))
            hand_values = [card.number for card in hand_copy]
            
            hand_suits = [s for _, s in sorted(zip(hand_values, hand_suits))]
            hand_values = sorted(hand_values)

            all_hands.append(hand_copy)

            if self._isRoyalFlush(hand_suits, hand_values):
                value_list.append(10)
            elif self._isStraightFlush(hand_suits, hand_values):
                value_list.append(9)
            elif self._isFourOfAKind(hand_suits, hand_values):
                value_list.append(8)
            elif self._isFullHouse(hand_suits, hand_values):
                value_list.append(7)
            elif self._isFlush(hand_suits, hand_values):
                value_list.append(6)
            elif self._isStraight(hand_suits, hand_values):
                value_list.append(5)
            elif self._isThreeOfAKind(hand_suits, hand_values):
                value_list.append(4)
            elif self._isTwoPair(hand_suits, hand_values):
                value_list.append(3)
            elif self._isPair(hand_suits, hand_values):
                value_list.append(2)
            else:
                value_list.append(1)

        return max(value_list)

    def _isFlush(self, suit_list, value_list):
        if len(suit_list) == 1:
            return True
        else:
            return False

    def _isStraight(self, suit_list, value_list):
        return value_list == list(range(value_list[0], value_list[-1] + 1))

    def _isStraightFlush(self, suit_list, value_list):
        if self._isStraight(suit_list, value_list) and self._isFlush(suit_list, value_list):
            return True
        else:
            return False

    def _isRoyalFlush(self, suit_list, value_list):
        if self._isStraight(suit_list, value_list) and self._isFlush(suit_list, value_list) and value_list[0] == 10:
            return True
        else:
            return False

    def _isPair(self, suit_list, value_list):
        value_dict = {}
        for value in value_list:
            if value not in value_dict:
                value_dict[value] = 1
            else:
                value_dict[value] += 1
        if 2 in value_dict.values():
            return True
        else:
            return False

    def _isTwoPair(self, suit_list, value_list):
        value_dict = {}
        for value in value_list:
            if value not in value_dict:
                value_dict[value] = 1
            else:
                value_dict[value] += 1
        if sorted(value_dict.values()) == [1,2,2]:
            return True
        else:
            return False

    def _isThreeOfAKind(self, suit_list,  value_list):
        value_dict = {}
        for value in value_list:
            if value not in value_dict:
                value_dict[value] = 1
            else:
                value_dict[value] += 1
        if 3 in value_dict.values():
            return True
        else:
            return False

    def _isFourOfAKind(self, suit_list,  value_list):
        value_dict = {}
        for value in value_list:
            if value not in value_dict:
                value_dict[value] = 1
            else:
                value_dict[value] += 1
        if 4 in value_dict.values():
            return True
        else:
            return False

    def _isFullHouse(self, suit_list,  value_list):
        if self._isPair(suit_list, value_list) and self._isThreeOfAKind(suit_list, value_list):
            return True

    def handCardAmt(self):
        return len(self.hand)

    def tieWon(self, other):
        if self.hand[0].number > other.hand[0].number:
            return True
        else:
            return False

    def __str__(self):
        return "     ".join([str(card) for card in self.hand])

    def __contains__(self,obj):
        if obj in self.hand:
            return True
        else:
            return False

    def __iter__(self):
        return iter(self.hand)