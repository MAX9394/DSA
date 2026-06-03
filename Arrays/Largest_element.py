# A = [13,46,24,52,20,9]
A = list(map(int, input().split()))

def largest_element(A:list) -> int:
    # return max(A)
    max_element = A[0]
    for i in range(len(A)):
        max_element = A[i] if A[i] > max_element else max_element
    return max_element

print(largest_element(A))