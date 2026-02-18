n = int(input())
x="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
    for j in range(i+1):
        print(x[j], end=" ")
    print()