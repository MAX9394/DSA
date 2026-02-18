n = int(input())

for i in range(n):
    if i == n-1 or i == 0:
        print(n*"* ", end = "")
    else:
        print("* "+(n-2)*"  "+"* ", end = "")
    print()