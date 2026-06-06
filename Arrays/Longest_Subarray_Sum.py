# Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.
# nums = [10, 5, 2, 7, 1, 9], k = 15

arr = list(map(int, input().split()))
k = int(input())

def func(arr:list, k:int) -> int:
    sum_sub_arr = 0
    len_sub_arr = 0
    n = len(arr)

    i, j = 0, 1
    while j >= i and i < n:
        sum_sub_arr = sum(arr[i:j])
        if sum_sub_arr < k and j < n:
            j = j + 1
        elif sum_sub_arr > k:
            i = i + 1
        else:
            len_sub_arr = max(len_sub_arr, j - i)
            i = i + 1
    # if j == n and sum_sub_arr != k:
    #     return 0
    return len_sub_arr

print(func(arr, k))