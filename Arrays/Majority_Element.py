# Given an integer array nums of size n, return the majority element of the array. The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.
# arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]
arr = list(map(int, input().split()))

def major_element(arr:list, n:int):
    arr.sort()
    return arr[n//2]

def major_element_2(arr:list):
    count = 0
    for i in range(len(arr)):
        if count == 0:
            element = arr[i]
        elif arr[i] == element:
            count += 1
        else:
            count -= 1
    return element

print(major_element_2(arr))