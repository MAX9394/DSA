n = int(input())
x="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n-1,-1,-1):
    for j in range(n-i,0,-1):
        print(x[n-j], end=" ")
    print()