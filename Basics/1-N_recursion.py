n = int(input())
x = 0

def recursion_print(x):
    if n == x:
        return
    else:
        print(x+1)
        recursion_print(x+1)

recursion_print(x)