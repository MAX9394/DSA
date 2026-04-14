# A = [13,46,24,52,20,9]
A = list(map(int, input().split()))

def Bubble_sort(A:list, n:int):
    if n <= 1:
        return A
    for i in range(n-1):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
    return Bubble_sort(A, n-1)

print(Bubble_sort(A, len(A)))