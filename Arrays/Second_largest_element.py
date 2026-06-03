# A = [13,46,24,52,20,9]
A = list(map(int, input().split()))

def largest_2nd_element(A:list):
    if len(A) <= 1:
        return -1
    if A[0] > A[1]:
        max1, max2 = A[0], A[1]
    else:
        max1, max2 = A[1], A[0]
    for i in range(1,len(A) - 1):
        if A[i] > max1:
            max1, max2 = A[i], max1
    return max2

print(largest_2nd_element(A))