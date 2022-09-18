# Report on Final Project

## Introduction

To many, Poker is considered a game of pure luck. Sometimes, you have a good hand you can call continuously; other times, you have such a terrible hand that you would consider fold right when you look at it.

However, poker is not completely determined by pure luck. Each hand, at each deal, at each cards on the board, has some chance of winning.

Monte Carlo is a method used to solve deterministic problem (in this case, consider either you have a winning chance or not) using randomness. Using this method, one can consider a hand good or not more reliably while playing, with chances of winning known.

In this project, the main consideration is the odd of winning of a hand of two cards given five cards dealt on the table under a number of players. For any two hands, if one is a sole player, the chances of winning is fixed - the player wins regardless of what he or she gets. However, since the game is commonly played by multiple people, the chances of winning are much harder to determine. Therefore, this project will rely on Monte Carlo to determine the winning chances of a hand of a player considering the overall table.


## Poker

Poker is a family of card games where players wager an amount of currency on whether their hand being the best hand or not. In this project, "Poker" refers to the classic poker game, where we are playing with 52 cards, each player will be dealt 2 cards, and initially the table will have three community cards, with 2 more being gradually dealt over the course of the game. Additionally, this version uses the high rule, in which Ace (A) is the highest ranked card.

There are ten possibilities of how a player's hand end up after 5 community cards are shown, ranked from best to worst:
- Royal Flush: This only happens when the player's hand, combine with the community cards, create a chain of A-K-Q-J-10, all in the same suit.
- Straight Flush: A chain of consecutive cards, all in the same suit.
- Four of a kind: Four cards having same rank.
- Full house: This is made up by having a three of a kind and a pair of different rank.
- Flush: 5 cards of the same suit, doesn't have to be in a consecutive order.
- Straight: A chain of consecutive cards, but not necessarily needed to be in the same suit.
- Three of a kind: Three cards having same rank
- Two pairs: Two pairs with different ranks
- Pair: Two cards having same ranks
- High card: Lowest possible hand, with no higher-levelled combinations can be made.

In this project, since there are 10 different types of hands, I assigned each type to a score.

Specifically,
- Royal Flush will have the score of 10.
- Straight Flush will have the score of 9.
- Four of a kind will have the score of 8.
- Full house will have the score of 7.
- Flush will have the score of 6.
- Straight will have the score of 5.
- Three of a kind will have the score of 4.
- Two pairs will have the score of 3.
- Pair will have the score of 2.
- High card hands will have the score of 1

The player will win when and only when that player has the hand with the highest score. In the case of tie, a tie breaker will occur, with the player with the best hand wins (as in, the player with cards of better ranks wins).

## Monte Carlo

Monte Carlo is a method used to predict the probability of different outcomes when random elements exist in the problem. Poker game is a game of "chance", that is, if the deck has ```x``` amount of cards left, the current player has 1/```x``` chance of getting a desired card shown on the table as a community card. As a result, Poker can be classified as a problem with random elements occuring within the problem.

In this project, I am interested in seeing the probability of a hand winning the game.

My methodology for determining this is as follows: Given the number of games that is being simulated and the number of players (including the one we are considering), I can check for each game if the player wins or not (the win condition has been briefly described above). 

If the player wins, the overall win counter is added by 1. At the end of the simulation, the rate of winning is determined by having the number of wins divided by the total amount of times simulated.

## Parallelization

To parallelize this, I will rely on MPI.
- The root processor will handle the generation/parsing of the community cards and hand cards.
- All processors will perform the same amount of rounds, and the root processor will have all the number of wins added from all processors,
- The rate of winning is calculated at root processor, with the total number of wins divided by the number of rounds simulated.

## Caveat

- It is very hard to avoid duplicate rounds being generated when a large amount of rounds are being simulated, in both serial and parallel implementations. While it is possible to have a "check" to see if a round has been generated or not, having one such check will increase run time by a lot. As a result, for the purpose of making only a simple simulator, I will not include a check for duplicate rounds. Seeding could potentially solve the randomization issues between rounds, but when the program runs in parallel for a large enough amount of times, the offset created by being in different ranks does not mean much anymore, and the overall rate will the same regardless of how many more rounds simulated and the number of processors used. 

- Since this is a Monte Carlo simulation, the more processors used, the more time will be needed to run the same program. This is due to the fact that all workers have to do the same amount of work. As a result, when comparing "speedup", I will consider the speedup, if exist, from running the parallel version in comparison to the serial version.

## Program Usage

After the project is pulled, users can run the program by running either of the commands in either versions (after cd to the folder):
- Serial version:
    + Fixed version with premade files
```
python3 ./main_serial.py fixed /path/to/file/with/comm_card_info.txt /path/to/file/with/hand_card_info.txt num_players num_rounds
```
       
    + Randomized version

```
python3 ./main_serial.py random num_players num_rounds seed
```
- Parallel version:
    + Fixed version with premade files
```
mpirun -np num_procs python3 ./main_parallel.py fixed /path/to/file/with/comm_card_info.txt /path/to/file/with/hand_card_info.txt num_players num_rounds
```

    + Randomized version

```
mpirun -np num_procs python3 ./main_parallel.py random num_players num_rounds seed
```


## Design decisions and rationale for those decisions

### Design decisions
- Python instead of C
- Usgae of seeds
- Deck, playing hand, and community cards have different classes used as representation.
- There are two ways user can use the program: 
    + Running the program with pre-made text files that specify the community cards and hand cards.
    + Allow the program to randomize the community cards and hand cards.
- Usage of timeit.defaulttimer() rather than other timing ultilites.
- Users can specify the number of players.
- The format of the txt files is as follows:
```
H, 8
S, 2
D, A
C, K
```

Most variations of the above will work, as long as the numbers are not spelled out as word and the letter-based cards (Ace, King, etc) are not translated to numerical values (as in, instead of K, the rank is 13).

These will work
```
Hearts, 8
Spades, 2
Diamonds, Ace
Club, King
```

but these won't
```
Hearts, eight
Spades, two
Diamonds, Ace
Club, 13
```

### Rationale
- Python instead of C

This is because I find Python to be somewhat more flexible and cleaner-looking in various aspects of this project. Specifically, since I can overwrite magic methods in Python, handling different classes in a Pythonic way can be more convinient and compact. Additionally, I can ultilize Python functionalities to make my code look cleaner and easy to read. 

- Usage of seeds
Seeds will, at least, make my testing more consistent in terms of what is generated, making evaluation easier.

- Deck, playing hand, and community cards have different classes used as representation.

Needless to say much, this is to make the code clearer.

- There are two ways user can use the program: 
    + Running the program with pre-made text files that specify the community cards and hand cards.
    + Allow the program to randomize the community cards and hand cards.
- The format of the txt files is as follows:
```
H, 8
S, 2
D, A
C, K
```

Most variations of the above will work, as long as the numbers are not spelled out as word and the letter-based cards (Ace, King, etc) are not translated to numerical values (as in, instead of K, the rank is 13).

These will work
```
Hearts, 8
Spades, 2
Diamonds, Ace
Club, King
```

but these won't
```
Hearts, eight
Spades, two
Diamonds, Ace
Club, 13
```

Originally, I thought that I wanted the user to put in the card informations. However, there is a problem to that particular implementation: The entire command line will be far too messy and hard to read.

If I were to carry on with that idea, a sample command line will be
```
mpirun -np 4 python3 ./main_parallel.py --comm H|3 S|K C|9 D|7 S|2 --hand D|3 D|4 10 100000
```
This would be very hard to keep track, due to all abbreviations, alongside with a lot of time cost just to type out one command and complication in code just to parse the command. Sure, I can use argparse to simplify the parsing, but that still means that I'm adding a lot of unnecessary complications to the program

As a result, I decided to simplify the inputs: One can put in the card information for community cards and player hand cards in .txt files in formats specified above. Of course, the user still has to keep track of the input cards, but it is far easier to look at cards line-by-line rather than looking the information in one straight line. Additionally, not a lot of code is needed to read and parse what is in the files.

As to why there is a randomized option, this is mostly for when user don't want to think about what to put in external txt files and just want to see the simulation result immediately.

- Usage of timeit.default_timer() rather than other timing ultilites.

I personally find the idea of the function finding the best timer to measure time appealing for usage, so that's the reason. Even when in further Python versions, timeit.default_timer() defaults to time.perf_counter(), [time.perf_counter() essentially does the similar thing](https://docs.python.org/3/library/time.html#time.perf_counter). 

- Users can specify the number of players.

This is so that the simulation can accurately represent the chances of winning at x amount of players, rather than bundling the data when considering from 1 to x amount of players.

## Original Goals
- [x] Bronze: Finish serial version of the simulation 
- [x] Silver: Finish parallel version of the simulation
- [] Gold: Finish C version of both

## Additional packages used

[mpi4py](https://mpi4py.readthedocs.io/en/stable/)

## Testing

In the folder PokerGamePython, there is a ```test``` folder. This folder contains test files for 2 cases: One where the rate of winning will always be 100% (Royal Flush) and one where the rate of winning will always be 0% (High Card but the cards are far too low to consider any winning chances). The program will be proven to run well and correct when those tests yields desirable results.

Other cases can be vary by number of rounds used for testing, so they can be very unreliable for testing. As a result, they are not used for correction verification.

```comm_cards.txt``` and ```hand_cards.txt``` are used for testing the 100% case, and ```comm_cards_0.txt``` and ```hand_card_0.txt``` are used for testing the 0% case

## Timing data

Notes:
- The timings are all in seconds (s)
- For timings in the fixed option, ```comm_cards.txt``` and ```hand_cards.txt``` are used.
- To make the timing matrices easier to look and evaluate, without loss of generality, the number of players are fixed to be 5.
- The testing is done on a VM instance of Ubuntu with 8 processors allocated for the VM.
- The CPU of the host machine is Intel i5-8250U.

### Serial version

Notes:
- The seeds are set to be the same to make sure that the same sets of cards are randomized every run. This also ensures that the received results can be interpreted more correctly.

- Fixed:

| num\_rounds | Time       | Rate   |
| :-----------: | :----------: | :------: |
| 100         | 0.27311    | 100.0% |
| 1000        | 3.31258    | 100.0% |
| 10000       | 27.450176  | 100.0% |
| 20000       | 54.14721   | 100.0% |
| 50000       | 134.038582 | 100.0% |
| 70000       | 203.936871 | 100.0% |
| 80000       | 279.481589 | 100.0% |
- Random:

| num\_rounds | Time       | Rate                |
| :-----------: | :----------: | :-------------------: |
| 100         | 0.302205   | 14.000000000000002% |
| 1000        | 2.605061   | 14.000000000000002% |
| 10000       | 29.255249  | 13.44%              |
| 20000       | 52.94756   | 13.73%              |
| 50000       | 130.677299 | 13.79%              |
| 70000       | 187.122983 | 13.69%              |
| 80000       | 209.827149 | 13.87%              |

### Parallel version

Notes:

- The column represents the number of processors used. Due to the fact that VM only has 8 cores allocated, at maximum 8 processes will be used. 
- The row represents the number of rounds used.
- The final column represents the winning rate
- The seeds are set to be the same to make sure that the same sets of cards are randomized every run. This also ensures that the received results can be interpreted more correctly.
- The rate shown is for when testing the program with 10000 rounds simulated.

Data:

- Fixed

|   | 100      | 1000     | 10000     | Rate   |
| :-: | :--------: | :--------: | :---------: | :------: |
| 1 | 0.350887 | 3.105089 | 29.227456 | 100.0% |
| 2 | 0.388004 | 3.728273 | 36.70352  | 100.0% |
| 3 | 0.456181 | 4.985602 | 48.445956 | 100.0% |
| 4 | 0.57202  | 5.515904 | 55.007856 | 100.0% |
| 5 | 0.681451 | 6.381936 | 64.19707  | 100.0% |
| 6 | 0.775515 | 7.499691 | 75.712729 | 100.0% |
| 7 | 0.913284 | 8.602577 | 87.557544 | 100.0% |
| 8 | 1.100962 | 9.408845 | 92.514434 | 100.0% |

- Random

|   | 100      | 1000     | 10000     | Rate                |
| :-: | :--------: | :--------: | :---------: | :-------------------: |
| 1 | 0.312479 | 2.671284 | 27.231163 | 13.99%              |
| 2 | 0.310549 | 2.941109 | 30.36817  | 13.91%              |
| 3 | 0.395352 | 3.700917 | 37.323622 | 13.639999999999999% |
| 4 | 0.551863 | 5.082247 | 49.232536 | 13.43%              |
| 5 | 0.597219 | 5.436867 | 55.196134 | 14.069999999999999% |
| 6 | 0.660817 | 6.35328  | 62.598252 | 13.68%              |
| 7 | 0.74545  | 7.122494 | 72.716507 | 13.750000000000002% |
| 8 | 0.886754 | 8.100787 | 83.304519 | 13.819999999999999% |

### After-testing notes
- It takes far less time for the parallel program to run a simulation with ```x``` rounds and ```n``` processors than the same program with ```x*n``` rounds simulated. In some cases, the parallel version saves half of the time needed in the serial version, and in the cases where there are 7 or 8 processors used, the parallel version takes only a third of the time needed in the serial version. 
- During the testing times, because the simulated rounds are also randomized, I have tried to control the randomness by adding a seperate seed to each round of simulation on each instance, but the rate shown is the same. This is showing exactly what I have discussed in the Caveat section.


