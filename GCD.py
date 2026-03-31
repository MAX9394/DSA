n1, n2 = map(int, input().split())

def GCD(n1, n2):
    return(n1 if n2 == 0 else GCD(n2, n1 % n2))

print(GCD(n1,n2))