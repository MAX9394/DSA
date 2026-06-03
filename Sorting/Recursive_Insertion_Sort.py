# A = [13,46,24,52,20,9]
A = list(map(int, input().split()))

def rec_insertion_sort(A:list, n:int, i:int) -> list:
    if i == n:
        return A
    else:
        key = A[i]
        j = i-1
        while j>=0 and A[j]>key:
            A[j+1] = A[j]
            j-=1
        A[j+1] = key
        return rec_insertion_sort(A, n, i+1)

print(rec_insertion_sort(A, len(A), 1))