# Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers. If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

from itertools import permutations

# arr = [1,3,2]
arr = list(map(int,input().split(",")))

def func(arr:list):
    '''Brute Force approach'''
    perms = sorted(set(permutations(arr)))
    current = tuple(arr)

    n = len(perms)
    for i in range(n):
        if perms[i] == current:
            if i == n-1:
                return list(perms[0])
            return list(perms[i+1])
    return arr

def func2(arr:list):
    '''Optimal approach'''
    n = len(arr)
    for i in range(n-2,-1,-1):
        if arr[i] < arr[i+1]:
            break_point = i
            break
    for j in range(n-2,-1,-1):
        if arr[j] > arr[break_point]:
            arr[j], arr[break_point] = arr[break_point], arr[j]
            break
    arr[break_point:] = arr[break_point::-1]
    return arr

print(func2(arr))