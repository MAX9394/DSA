# A = [13,46,24,52,20,9]
A = list(map(int, input().split()))

def is_sorted(arr:list, n:int) -> bool:
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return False
    return True

print(is_sorted(A, len(A)))