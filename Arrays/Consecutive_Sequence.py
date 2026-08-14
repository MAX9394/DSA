# Given an array nums of n integers. Return the length of the longest sequence of consecutive integers. The integers in this sequence can appear in any order.

# arr = [0,3,7,2,5,8,4,6,0,1]
arr = list(map(int,input().split(",")))

def func(arr: list) -> int:
    '''Sorting, Good approach'''
    arr = sorted(arr)
    lastSmallest = float('-inf')
    count = 0
    max_count = 1

    for i in range(1,len(arr)):
        if arr[i] - 1 == lastSmallest:
            count += 1
        elif arr[i] != lastSmallest:
            count = 1
        lastSmallest = arr[i]
        max_count = max(max_count, count)
    
    return max_count

def func2(arr:list) -> int:
    '''Sort, Hashmap, iterate'''
    arr = sorted(arr)
    x = arr[-1] + 1
    hash_map = [0] * x

    for i in arr:
        hash_map[i] += 1
    
    count = 0
    max_count = 0

    for i in range(len(hash_map)):
        if hash_map[i] > 0:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

def func3(arr:list) -> int:
    '''Unordered set, hashnet'''
    arr_set = list(set(arr))
    count = 1
    longest = 1

    for i in arr_set:
        if (i - 1) in arr_set:
            count += 1
            longest = max(longest, count)
        else:
            count = 1
    
    return longest

print(func3(arr))