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

def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

print(least_difference(1, 10, 100))

# print(help(time))
help(print)