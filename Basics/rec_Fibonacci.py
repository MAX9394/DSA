# from functools import lru_cache

n = int(input())

# @lru_cache(None)
def Fibonacci(n):
    if n <= 1:
        return n
    return (Fibonacci(n-1) + Fibonacci(n-2))

print(Fibonacci(n))