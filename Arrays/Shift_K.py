# A = [13,46,24,52,20,9]
A = list(map(int, input().split()))

# def shift_k(arr:list, k:int) -> list:
#     n = len(arr)
#     k = k % n

#     if k > 0:
#         for i in range(k):
#             arr = rshift(arr)
#         return arr
#     elif k < 0:
#         for i in range(-k):
#             arr = lshift(arr)
#         return arr
    
#     return arr

# def lshift(arr:list) -> list:
#     # arr.append(arr.pop(0))
#     key = arr[0]
#     for i in range(len(arr)-1):
#         arr[i] = arr[i+1]
#     arr[-1] = key
#     return arr

# def rshift(arr:list) -> list:
#     key = arr[-1]
#     for i in range(len(arr)-1,0,-1):
#         arr[i] = arr[i-1]
#     arr[0] = key
#     return arr

# print(shift_k(A.copy(),4))

def optimized_shift_k(arr:list, k:int) -> list:
    n = len(arr)
    k = k % n

    arr = arr[::-1]
    arr[:k] = arr[:k][::-1]
    arr[k:] = arr[k:][::-1]
    
    return arr

print(optimized_shift_k(A.copy(),4))