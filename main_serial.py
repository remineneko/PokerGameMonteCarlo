from PokerGame import *
from Randomizer import *
from file_handling import *
from timeit import default_timer as timer
import sys

def fixedMode(comm_cards_fp, hand_cards_fp, deck:Deck):
    '''
    In fixed mode, we read the files, converts the data from the files to the proper cards, then the simulation is done.
    '''
    comm_cards = convert(comm_cards_fp, CommunityCard)
    hand_cards = convert(hand_cards_fp, PokerHand)
    deck.batchRemoveCards(comm_cards)
    deck.batchRemoveCards(hand_cards)
    return comm_cards, hand_cards

def randomizedMode(deck:Deck, seed):
    '''
    In randomized mode, we randomize the cards on the table and on the hand, then we do the simulation.
    '''
    return randomize_randomized(deck, seed)
    
def main(*args):
    new_deck = Deck()
    comm_cards, hand_cards = CommunityCard(), PokerHand()

    if len(args) > 5:
        print("Please check your input")
        exit()
    elif args[0] == 'fixed':
        comm_fp = args[1]
        hand_fp = args[2]
        num_players = int(args[3])
        num_rounds = int(args[4])
        comm_cards, hand_cards = fixedMode(comm_fp, hand_fp, new_deck)
        
    elif args[0] == 'random':
        num_players = int(args[1])
        num_rounds = int(args[2])
        try:
            args[3]
        except NameError:
            seed = None
        else:
            seed = int(args[3])
        comm_cards, hand_cards = randomizedMode(new_deck, seed)

    else:
        print("Please check your input")
        exit()


    print("The program will simulate with the following data:")
    print("Community Cards:")
    print(comm_cards)
    print("Player Hand:")
    print(hand_cards)
    print(f"Number of players: {num_players}")
    print(f"Number of rounds: {num_rounds}")

    num_players = int(num_players)
    num_rounds = int(num_rounds)
    start = timer()
    won = 0
    for i in range(num_rounds):
        used_deck = deepcopy(new_deck)
        other_players_hands = randomize_hands(num_players, used_deck)
        new_game = PokerGame(comm_cards, hand_cards, other_players_hands)
        if new_game.isPlayerWinner():
            won += 1

    end = timer()
    elapsed = round(end - start,6)

    rate = round(won/num_rounds,4) * 100
    print(f"The winning rate is: {rate}%")

    print(f"It takes {elapsed} seconds to run the linear simulator")



if __name__ == "__main__":
    main(*sys.argv[1:])