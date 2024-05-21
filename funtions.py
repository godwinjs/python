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