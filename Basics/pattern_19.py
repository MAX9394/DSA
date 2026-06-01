n = int(input())
for i in range(n):
    for ul in range(0,n-i):
        print("*", end=" ")
    for sp1 in range(i):
        print(4*" ", end="")
    for ur in range(n-i):
        print("*", end=" ")
    print()

for i in range(n):
    for ll in range(i+1):
        print("*", end=" ")
    for sp2 in range(n-i-1):
        print(4*" ", end="")
    for lr in range(i+1):
        print("*", end=" ")
    print()