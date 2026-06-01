n = int(input())
x=0
for i in range(n):
    for j in range(i+1):
        x+=1
        print(x, end=" ")
    print()