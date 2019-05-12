"""
In number theory, Wilson's theorem states that a natural number n > 1 
is a prime number if and only if the product of all the positive integers 
less than n is one less than a multiple of n. 
That is, the factorial (p-1)! + 1 divide on p
"""

import random
import math

def test():

    rnd = random.randint(2, 1000)
    result = (fact(rnd - 1) + 1) % rnd == 0
    print("Is number " + str(rnd) + " prime? \nAnswer - "+str(result))

def fact(p):
    if p == 1:
        return 1
    else:
        return p * fact(p-1)