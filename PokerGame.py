from Deck import *
from Hand import *
from CommunityCard import *
from typing import List
from collections import defaultdict
from copy import deepcopy

class PokerGame:
    def __init__(self, table: CommunityCard, player_hand: PokerHand, other_player_hands: List[PokerHand]):
        self.table = table
        self.player_hand = player_hand
        self.other_player_hands = other_player_hands

    def isPlayerWinner(self):
        other_copy = deepcopy(self.other_player_hands)
        other_copy.append(self.player_hand)
        score_dict = {player_hand:score for player_hand, score in zip(other_copy, [hand.evaluate(self.table) for hand in other_copy])}
        # for k, v in score_dict.items():
        #     print(k, ": ",v)
        max_val = max(list(score_dict.values()))
        new_dict = defaultdict(list)
        for k, v in score_dict.items():
            if v == max_val and k not in new_dict:
                new_dict[k] = v
        if len(new_dict) > 1:
            if self.player_hand not in new_dict:
                return False
            else:
                del new_dict[self.player_hand]
                winner = True
                all_rem_hands = list(new_dict.keys())
                ind = 0
                while winner and ind < len(all_rem_hands):
                    if not self.player_hand.tieWon(all_rem_hands[ind]):
                        winner = False
                    else:
                        ind+= 1
                if winner:
                    return True
                else:
                    return False
        elif list(new_dict.keys())[0] == self.player_hand:
            return True
        else:
            return False
        