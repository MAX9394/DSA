n = int(input())
x="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
    for k in range(n-i):
        print(" ", end=" ")
    for j in range(i):
        print(x[j], end=" ")
    for l in range(i,-1,-1):
        print(x[l],end=" ")
    print()