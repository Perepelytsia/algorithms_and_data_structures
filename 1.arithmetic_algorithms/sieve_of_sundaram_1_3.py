"""
Start with a list of the integers from 1 to n. From this list, remove all numbers of the form i + j + 2ij where:

    i , j ∈ N ,   1 ≤ i ≤ j {\displaystyle i,j\in \mathbb {N} ,\ 1\leq i\leq j} i,j\in\mathbb{N},\ 1 \le i \le j
    i + j + 2 i j ≤ n {\displaystyle i+j+2ij\leq n} i + j + 2ij \le n

The remaining numbers are doubled and incremented by one, giving a list of the odd prime numbers (i.e., all primes except 2) below 2n + 2.

The sieve of Sundaram sieves out the composite numbers just as sieve of Eratosthenes does, but even numbers are not considered; the work of "crossing out" the multiples of 2 is done by the final double-and-increment step. Whenever Eratosthenes' method would cross out k different multiples of a prime 2 i + 1 {\displaystyle 2i+1} 2i+1, Sundaram's method crosses out i + j ( 2 i + 1 ) {
"""

import random
import math

def test():

    N = 100
    print("\nmax number "+str(N))
    data = [x for x in range(1, N + 1)]
    for i in range(1, N + 1):
        if i <= math.floor((math.sqrt(2 * N + 1) - 1) / 2):
            #print('i'+str(i))
            for j in range(i, N + 1):
                if j <= math.floor((N - i) / (2 * i + 1)):
                    #print('j'+str(j))
                    digit = i + j + 2 * i * j
                    if digit <= N:
                        #print(digit)
                        if data.count(digit):
                            data.remove(digit)
    #print(data)
    for index, d in enumerate(data):
        data[index] = d * 2 + 1
    print("prime numbers")
    print(data)
