# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

nums = list(map(int, input().split(",")))

def function(nums:list) -> list:
    ans = []
    nums.sort()
    n = len(nums)
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]: continue
        
        j = i + 1
        k = n - 1
        
        while j < k:
            currentSum = nums[i] + nums[j] + nums[k]
            if currentSum == 0:
                ans.append([nums[i], nums[j], nums[k]])
                j = j + 1
                k = k - 1

                while j < k and nums[j] == nums[j-1]: j = j + 1
            elif currentSum < 0: j = j + 1
            else: k = k - 1
    return ans

print(function(nums))