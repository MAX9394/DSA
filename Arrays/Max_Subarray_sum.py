# Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.

# arr = [2, 3, 5, -2, 7, -4]

arr = list(map(int, input().split(", ")))

def func(arr:list) -> int:
    '''
    prints only sum of subarray
    '''
    n = len(arr)
    s = 0
    max_s = 0
    for i in range(n):
        if s < 0:
            s = 0
        else:
            s += arr[i]
        max_s = max(s, max_s)
    return max_s

def func2(arr:list):
    '''
    prints only sum and subarray
    '''
    n = len(arr)
    left = 0
    right = 0
    s = 0
    max_s = 0
    for i in range(n):
        if s < 0:
            s = 0
            temp = 0
            left = right = i+1
        else:
            temp = s + arr[i]
        
        if temp > s:
            right = i
            s = temp
        max_s = max(s, max_s)
    return max_s, arr[left:right+1]

def func3(arr:list) -> int:
    n = len(arr)
    total = 0
    max_total = float('-inf')
    for i in range(n):
        total += arr[i]
        max_total = max(max_total, total)

        if total < 0:
            total = 0
        
    return max_total

max_s, res_arr = func2(arr)
print(max_s)
print(res_arr)