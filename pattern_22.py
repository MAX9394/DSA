n = int(input())
m = n*2-1

for i in range(m):
    for j in range(m):
        print(n-min([i,j,m-1-i,m-1-j]), end = " ")
    print()
