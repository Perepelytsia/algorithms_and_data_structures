"""
The Greek mathematician Eratosthenes (3rd-century B.C.E) designed a quick way to find 
all the prime numbers. It’s a process called the Sieve of Eratosthenes. We’re going
to see how it works by finding all the prime numbers between 1 and 100. The idea is 
to find numbers in the table that are multiples of a number and therefore composite, 
to discard them as prime. The numbers that are left will be prime numbers. The Sieve 
of Eratosthenes stops when the square of the number we are testing is greater than 
the last number on the grid (in our case 100). Since 112  = 121 and 121>100, when 
we get to the number 11, we can stop looking
	
"""

import random
import math

def test():
    rnd = random.randint(2, 200)
    data = [x for x in range(1, rnd)]
    print("\nall numbers")
    print(data)
    for pr in range(1, math.floor(math.sqrt(rnd))):
    	for d in data:
    		if d != pr and d % pr == 0:
    			data.remove(d)
    print("\nprime numbers")
    print(data)