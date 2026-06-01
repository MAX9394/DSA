# A = [13,46,24,52,20,9]
A = list(map(int, input().split()))

def merge(left:list, right:list)-> list:
    result = []

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def merge_sort(A:list) -> list:
    if len(A) <= 1:
        return A
    middle = len(A) // 2
    left = merge_sort(A[:middle])
    right = merge_sort(A[middle:])

    return merge(left, right)

print(merge_sort(A))