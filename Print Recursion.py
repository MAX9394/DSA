n = int(input())

def recursion_print(n):
    if n == 0:
        return
    else:
        print("Recursion number", n)
        recursion_print(n-1)

recursion_print(n)