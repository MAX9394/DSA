# Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.
# arr = [4,1,2,1,2]
arr = list(map(int, input().split()))

# def not_pair(arr:list) -> int:
#     temp = []
#     for i in range(len(arr)):
#         if arr[i] in temp:
#             temp.remove(arr[i])
#         else:
#             temp.append(arr[i])
    
#     return temp[0]

def getSingle(arr:list):
    xorr = 0
    for num in arr:
        xorr ^= num
    return xorr

# print(not_pair(arr))
print(getSingle(arr))