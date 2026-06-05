# A = [13,46,24,52,20,9]
A = list(map(int, input().split()))

key = 9

print(A.index(key) if key in A else -1)