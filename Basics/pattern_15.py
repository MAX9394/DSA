n = int(input())
x="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
    for j in range(n-i):
        print(x[j], end=" ")
    print()