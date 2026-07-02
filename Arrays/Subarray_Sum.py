# Given an array containing both positive and negative integers, we have to find the length of the longest subarray with the sum of all elements equal to zero.
# arr = [6, -2, 2, -8, 1, 7, 4, -10]
arr = list(map(int, input().split()))

def subarray_sum(arr: list, target = 0):
    n = len(arr)
    max_len = 0
    for j in range(n,0,-1):    
        for i in range(j+1):
            if sum(arr[i:j]) == 0:
                max_len = max(max_len, len(arr[i:j]))
    return max_len

# print(subarray_sum(arr, 0))

def subarray_sum_2(arr: list, target = 0):
    n = len(arr)
    max_len = 0
    s = 0
    hashmap : dict[int,int] = {}
    for i in range(n):
        s += arr[i]
        if s == target:
            max_len = i + 1
        elif s in hashmap:
            max_len = max(max_len, i-hashmap[s])
        else:
            hashmap[s] = i
    return max_len

print(subarray_sum_2(arr))