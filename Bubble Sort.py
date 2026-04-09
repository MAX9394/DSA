# A = [13,46,24,52,20,9]
A = list(map(int, input().split()))

def Bubble_sort(A: list, n: int) -> list:
    for i in range(n-1,0,-1):
        for j in range(i):
            if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

print(Bubble_sort(A, len(A)))
