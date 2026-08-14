# Implement pow(x, n), which calculates x raised to the power n (i.e. x^n).

x = float(input())
n = int(input())

def func(x:float,n:int):
    '''Limits of n equals to int limits. Therefore normal loop function doesn't work here'''

    if n == 0: return 1
    if n == 1: return x
    if n == -1: return 1/x
    if x == 0: return 0
    if x == 1: return 1
    if x == -1 and n%2 == 0: return 1
    if x == -1 and n%2 == 1: return -1

    binForm = n
    if binForm < 0:
        x = 1 / x
        binForm = - binForm
    ans = 1

    while binForm > 0:
        if binForm % 2 == 1:
            ans = ans * x
        x = x ** 2
        binForm = binForm // 2
    
    return ans

print(func(x,n))