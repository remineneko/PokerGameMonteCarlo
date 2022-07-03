from Card import Card
from Deck import Deck
from Hand import PokerHand
from CommunityCard import CommunityCard


def randomize_comm_cards(deck:Deck, seed):
    new_comm_cards = CommunityCard()
    comm_card_limit = new_comm_cards.comm_card_amt_limit
    for i in range(comm_card_limit):
        new_comm_cards.addCard(deck.getTopCard())
        deck.shuffle(seed)
    return new_comm_cards

def randomize_hand(deck:Deck, seed = None):
    new_hand_cards = PokerHand()
    hand_card_limit = new_hand_cards.hand_limit
    for i in range(hand_card_limit):
        new_hand_cards.addCard(deck.getTopCard())
        deck.shuffle(seed)
    return new_hand_cards

def randomize_hands(player_count, deck:Deck):
    all_players_hands = []
    for i in range(player_count - 1):
        all_players_hands.append(randomize_hand(deck))
    return all_players_hands


def randomize_randomized(deck:Deck, seed):
    return randomize_comm_cards(deck, seed), randomize_hand(deck, seed)
    
            
            
            
    
