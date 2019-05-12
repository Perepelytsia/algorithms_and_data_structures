"""
Must be without division!!!
Sieve of Eratosthenes is a simple and ancient algorithm used to find the prime numbers up to any given limit. It is one of the most efficient ways to find small prime numbers. For a given upper limit the algorithm works by iteratively marking the multiples of primes as composite, starting from 2. Once all multiples of 2 have been marked composite, the muliples of next prime, ie 3 are marked composite. This process continues until where is a prime number. 

"""

import random
import math

def test():

    rnd = 100#random.randint(2, 200)
    print("\nmax number " +str(rnd))
    rnd += 1
    data = [x for x in range(2, rnd)]

    #print("all numbers")
    #print(data)
    
    for index, digit in enumerate(data):
        if digit != 0 and digit ** 2 <= rnd - 1:
            #print("Next" + str(digit))
            step = index + digit 
            while step < len(data):
                if data[step] != 0:
                    #print(data[step])
                    data[step] = 0
                step += digit
    
    print("prime numbers")
    print(data)
