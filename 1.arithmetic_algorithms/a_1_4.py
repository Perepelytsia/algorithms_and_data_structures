"""
1. Выписываются все натуральные числа из диапазона от 1 до n
2. Перебираются все возможные пары чисел x, y, где x<=sqrt(n) и y<=sqrt(n). Т.е. (1,1), (1,2),…, (1,sqrt(n)), (2,1), (2,2),…, (sqrt(n),sqrt(n))
3. Для каждой пары чисел вычисляются значения следующих трех уравнений:
   a) {(x,y): x > 0, y > 0; 4x^2 + y^2 = n}  – нечетно
   b) {(x,y): x > 0, y > 0; 3x^2 + y^2 = n}  – нечетно
   c) {(x,y): x > y > 0; 3x^2 - y^2 = n}     – нечетно
4. Для каждого вычисленного значения уравнений вычисляются остатки от деления на 12, причем
   a) если остаток равен 1 или 5 для значения первого уравнения;
   b) если остаток равен 7 для значения второго уравнения;
   с) если остаток равен 11 для значения третьего уравнения.
   То в исходном ряду чисел от 1 до n число помечается как простое.
   Замечание: если какое-то число Z присутствует в значениях нескольких уравнений (допустим a и b), 
   и остаток от деления на 12 этого числа удовлетворяет условиям обоих групп, то число помечается два раза: 
   сначала как простое, а потом как составное.
5. На последнем этапе проверяется кратность помеченных чисел квадратам простых чисел из диапазона от 5 до sqrt(n). 
   Если число кратно квадрату, то оно помечается как составное. 
"""

import random
import math

def test():

    N = 100
    rangeData = range(1,math.floor(math.sqrt(N)))
    data = set()
    print("\nmax number "+str(N))

    for x in [x for x in rangeData]:
        for y in [y for y in rangeData]:
            
            digit = 4 * (x ** 2) + (y ** 2) 
            if checkRest(N, digit, [1, 5]):
                data.add(digit)

            digit = 3 * (x ** 2) + (y ** 2)
            if checkRest(N, digit, [7]):
                data.add(digit)
            if x > y:
                digit = 3 * (x ** 2) - (y ** 2)
                if checkRest(N, digit, [11]):
                    data.add(digit)

    data.add(2)
    data.add(3)
    data.add(5)
     
    for d in data:
        d2 = d ** 2
        n = d2
        while(n < N):
            if n in data:
                data.discard(n)
            n += d2

    print("prime numbers")
    print(data)

def checkRest(N, number, rest):
    if number < N and number % 2 and number % 3 and number % 5 and number % 7:
        if number % 12 in rest:
            return True
    return False
