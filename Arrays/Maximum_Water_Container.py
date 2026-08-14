# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# arr = [1,8,6,2,5,4,8,3,7]

arr = list(map(int, input().split(",")))

def function(arr:list)-> int:
    left = 0
    right = len(arr) - 1
    max_capacity = 0
    while left < right:
        capacity = min(arr[left], arr[right]) * (right - left)
        max_capacity = max(max_capacity, capacity)

        if arr[left] > arr[right]:
            right -= 1
        else:
            left += 1
    return max_capacity

print(function(arr))