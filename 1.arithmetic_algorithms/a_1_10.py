"""
Find x, y in the equal: a*x + b*y = gcd(a,b)
"""

import random
import math

def test():
    a = random.randint(1,1000)
    b = random.randint(1,1000)
    print("Numbers: " + str(a) + " and "+str(b))
    print("GCDEX: "+ str(gcdex(a,b)))

def gcd(a: int, b: int):
    if b == 0: return a
    else: return gcd(b, a % b)

def gcdex(a :int, b: int):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdex(b, a % b)
        print(str(d) + " " + str(x) +" "+ str(y))
        return d, y, x - y * (a // b)
