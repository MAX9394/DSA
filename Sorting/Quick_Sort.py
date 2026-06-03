# A = [13,46,24,52,20,9]
A = list(map(int, input().split()))

def quick_sort(A:list, low:int, high:int):
    if low < high:
        pivot = partition(A, low, high)
        quick_sort(A, low, pivot - 1)
        quick_sort(A, pivot + 1, high)
        return A

def partition(A:list, low:int, high:int) -> int:
    pivot = A[high]
    i = low - 1

    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]
    return i+1

print(quick_sort(A, 0, len(A)-1))