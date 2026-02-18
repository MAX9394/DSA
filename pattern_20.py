n = int(input())

for u in range(n):
    for ul in range(u+1):
        print("*", end = " ")
    for usp in range(n-u-1):
        print(4*" ", end = "")
    for ur in range(u+1):
        print("*", end = " ")
    print()

for l in range(n-1):
    for ll in range(n-l-1):
        print("*", end = " ")
    for lsp in range(1, l+2):
        print(4*" ", end = "")
    for lr in range(n-l-1):
        print("*", end = " ")
    print()
