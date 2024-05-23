from __future__ import print_function
import sys
fp = sys.stdout
print("Do you want to continue (Y/n): ", end="")
fp.flush()  # Uncomment this line to see the prompt immediately

import time
while True:
    #print("great output as always")
    print("great output as always", flush=True)
    #time.sleep(2)
    break

#defining functions
def least_difference(a, b, c):
    # using docstrings to make help function return a nice info of my function
    # based on say the idiot no smart enough to read my function know whatsup
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
# Function that doesn't have return statement dislays none when called similar to null
# Other examples of useful side effects include writing to a file, calling extrnal DB or modifying an input.

print(
    least_difference(1, 10, 100), #9 0 1
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
)

# print(help(time))
help(print)

def greet(who="Colin"):
    print("Hello,", who)
    
greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")
#Hello, Colin
#Hello, Kaggle
#Hello, world

# args as functions
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)
# 5
# 25

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)
#100
#14
total_candies = 1

print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")

"""
In this problem we'll be working with a simplified version of blackjack (aka twenty-one). In this version there is one player (who you'll control) and a dealer. Play proceeds as follows:

The player is dealt two face-up cards. The dealer is dealt one face-up card.
The player may ask to be dealt another card ('hit') as many times as they wish. If the sum of their cards exceeds 21, they lose the round immediately.
The dealer then deals additional cards to himself until either:
the sum of the dealer's cards exceeds 21, in which case the player wins the round
the sum of the dealer's cards is greater than or equal to 17. If the player's total is greater than the dealer's, the player wins. Otherwise, the dealer wins (even in case of a tie).
When calculating the sum of cards, Jack, Queen, and King count for 10. Aces can count as 1 or 11 (when referring to a player's "total" above, we mean the largest total that can be made without exceeding 21. So e.g. A+8 = 19, A+8+8 = 17)

For this problem, you'll write a function representing the player's decision-making strategy in this game. We've provided a very unintelligent implementation below:

add Codeadd Markdown

add Codeadd Markdown
This very conservative agent always sticks with the hand of two cards that they're dealt.

We'll be simulating games between your player agent and our own dealer agent by calling your function.

Try running the function below to see an example of a simulated game:

add Codeadd Markdown
q7.simulate_one_game()
add Codeadd Markdown
The real test of your agent's mettle is their average win rate over many games. Try calling the function below to simulate 50000 games of blackjack (it may take a couple seconds):

add Codeadd Markdown
q7.simulate(n_games=50000)
add Codeadd Markdown
Our dumb agent that completely ignores the game state still manages to win shockingly often!

Try adding some more smarts to the should_hit function and see how it affects the results.

add Codeadd Markdown

​
q7.simulate(n_games=50000)
"""

def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    return False

def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    return False


x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)