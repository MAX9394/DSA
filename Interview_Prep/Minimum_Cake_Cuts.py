# Given two integers N (number of cakes) and M (number of people), determine the minimum number of cuts required so that each person receives an equal share of the cake.

cakes = int(input())
people = int(input())

import math

def func(n:int, m:int):
    if n == m:
        return 0
    elif n > m:
        n = n % m
    # cakes_div = m/n
    pieces = math.ceil(m/n)

    return (pieces-1)*n

print(func(cakes, people))