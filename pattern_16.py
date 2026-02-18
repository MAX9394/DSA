n = int(input())
x="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
    for k in range(i+1):
        print(x[i], end=" ")
    print()