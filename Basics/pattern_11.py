n = int(input())
for i in range(n):
    for j in range(i+1): 
        print(1-((i+j)%2), end=" ")
    print()