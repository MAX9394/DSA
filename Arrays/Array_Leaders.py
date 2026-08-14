# Given an array, return leaders. Leader of an array is rightmost element as well as every element which is greater than all the elements to its right.

# arr = [10,22,12,3,0,6]
arr = list(map(int, input().split(",")))

def func(arr:list) -> list:
    if not arr:
        return []
    
    max_elem = float('-inf')
    res = []

    for i in range(len(arr)-1, -1, -1):
        if arr[i] > max_elem:
            max_elem = arr[i]
            res.append(arr[i])

    # res.append(k)
    return res[::-1]

print(func(arr))