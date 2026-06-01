# A = [13,46,24,52,20,9]
A = list(map(int, input().split()))

def SelectionSort(A: list, n: int) -> list:
    for i in range(n):
        min_index = i
        for j in range(i,n):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

print(SelectionSort(A, len(A)))