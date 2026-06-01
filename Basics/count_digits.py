import math

n = int(input())

if n == 0:
    print(1)
else:
    print(int(math.log10(n)) + 1)