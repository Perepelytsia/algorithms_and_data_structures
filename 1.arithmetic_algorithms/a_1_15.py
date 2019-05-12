"""
Пусть n=p⋅q – известное целое число, являющееся произведением двух неизвестных простых чисел 
p и q, которые требуется найти. Большинство современных методов факторизации основано на идее, предложенной еще Пьером Ферма, заключающейся в поиске пар натуральных чисел 
A и B таких, что выполняется соотношение:
n=x^2 - y^2 = (x-y)(x+y)
"""

import random
import math

def test():

    n = random.randint(2, 1000)
    sqrt = math.floor(math.sqrt(n))
    k = 1
    iteration = True
    while True:
        print(k)
        if k > 1000000:
            break
        x = sqrt + k
        y = math.sqrt(((x) ** 2) - n)
        if not y - int(y):
            a = x + y
            b = x - y
            print("Numbers: x=" + str(x) + " y="+ str(y) +" a="+ str(a) +" b="+ str(b))
            break
        k += 1
    print("Number - " +str(n))