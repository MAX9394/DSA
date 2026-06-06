# Given an array of integers arr[] and an integer target. Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.
# arr[] = {2,6,5,8,11}, target = 14

arr = list(map(int, input().split()))
k = int(input())

# def two_sum(arr:list,k:int) -> bool:
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(i+1,n):
#             if arr[i]+arr[j] == k:
#                 return True
#     return False

def two_sum_2(arr:list, target:int) -> bool:
    arr = sorted(arr)
    left, right = 0, len(arr)-1

    while left<right:
        k = arr[left] + arr[right]
        
        if k > target:
            right -= 1
        elif k < target:
            left += 1
        else:
            return True
    return False

# print(two_sum(arr,k))
print(two_sum_2(arr,k))