"""
 u and v are the same. For this condition, the GCD is the same as any of the two numbers.
Value of u is 0. Then the GCD is v.
Value of v is 0. GCD will be u.
u is even v is even. Then the GCD of the two numbers will be 2*gcd(u/2, v/2)(Because 2 is the common factor). So here we are using the recursive function call.
u is even v is odd. In this case GCD will be gcd(u/2, v)(Because 2 is never gonna make into the value of GCD). Again a recursive functional call.
u is odd v is even. GCD will be gcd(u, v/2)(Similar to the above case).
u is odd v is odd and u > v. Then the GCD will be gcd((u-v)/2, v). This case is to ensure that the input given to the gcd function will not be a negative integer.
u is odd v is odd and u < v. GCD will be gcd((v-u)/2, u). This case is similar to the above one
"""

import random
import math

def gcd(u, v):
    if u == v:
        return u
    elif u == 0:
        return v
    elif v == 0:
        return u
    # u is even
    elif u & 1 == 0:
        # v is even
        if v & 1 == 0:
            return 2*gcd(u >> 1, v >> 1)
        # v is odd
        else:
            return gcd(u >> 1, v)
    # u is odd
    elif u & 1 != 0:
        # v is even
        if v & 1 == 0:
            return gcd(u, v >> 1)
        # v is odd and u is greater than v
        elif u > v and v & 1 != 0:
            return gcd((u-v) >> 1, v)
        # v is odd and u is smaller than v
        else:
            return gcd((v-u) >> 1, u)

def test():
    u = random.randint(1,100)
    v = random.randint(1,100)
    print("Numbers: " + str(u) + " and "+str(v))
    result = gcd(u, v)
    print("GCD", result)
