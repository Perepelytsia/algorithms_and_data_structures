import random
import math

def test():
    rnd = 100#random.randint(2, 200)
    print("\nmax number "+str(rnd))
    rnd += 1
    data = [x for x in range(1, rnd)]
    for pr in range(1, rnd):
        for d in data:
            if d != pr and d % pr == 0:
                data.remove(d)
    print("prime numbers")
    print(data)
