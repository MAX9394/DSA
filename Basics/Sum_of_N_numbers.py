n = int(input())
sum_n = 0

def recursion_print(n, sum_n):
    if n == 0:
        return sum_n
    else:
        return recursion_print(n-1, sum_n + n)

print(recursion_print(n, sum_n))