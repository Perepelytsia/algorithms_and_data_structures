"""
The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number.
Since this replacement reduces the larger of the two numbers, repeating this process gives successively smaller pairs of numbers until the two numbers become equal.
When that occurs, they are the GCD of the original two numbers.
"""

import random
import math

def test():

    a = random.randint(1,1000)
    b = random.randint(1,1000)
    print("Numbers: " + str(a) + " and "+str(b))

    while a != b:
        if a < b:
            a,b = b,a
        a = a - b        
 
    print("GCD - "+ str(a))
