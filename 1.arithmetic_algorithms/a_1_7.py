"""
Fermat's little theorem states that if p is a prime number, 
then for any integer a, the number ap − a is an integer multiple of p. 
In the notation of modular arithmetic, this is expressed as
(a^p-1) mod for p = 1
"""

import random
import math

def test():

    p = random.randint(2, 100)
    result = True
    i = 4
    while i > 0:
    	a = random.randint(2, 100)
    	result = (a**(p-1)) % p == 1
    	i -= 1
    	if not result:
    		break
    print("Number " + str(p) + " must be prime? \nAnswer - "+str(result))