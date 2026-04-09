# A = [13,46,24,52,20,9]
A = list(map(int, input().split()))

def Insertion_Sort(A: list, n:int) -> list:
    for i in range(1,n):
        key = A[i]
        j = i-1
        
        while j >=0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

print(Insertion_Sort(A,len(A)))