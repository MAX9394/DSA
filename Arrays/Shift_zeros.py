# A = [1,0,2,3,0,4,0,1]
A = list(map(int, input().split()))

def shift_zeros(arr:list):
    for i in range(arr.count(0)):
        arr.remove(0)
        arr.append(0)   
    return arr
    
def moveZeroes(nums):
    # Pointer to the first zero
    j = nums.index(0) if 0 in nums else -1

    # Find the first zero
    # for i in range(len(nums)):
    #     if nums[i] == 0:
    #         j = i
    #         break

    # If no zero found, return
    if j == -1:
        return

    # Start from the next index of first zero
    for i in range(j + 1, len(nums)):
        # If current element is non-zero
        if nums[i] != 0:
            # Swap with nums[j]
            nums[i], nums[j] = nums[j], nums[i]
            # Move j to next zero
            j += 1
    return nums

print(shift_zeros(A.copy()))
print(moveZeroes(A.copy()))