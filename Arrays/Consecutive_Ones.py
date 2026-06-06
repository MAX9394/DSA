# arr = [1, 1, 0, 1, 1, 1]
arr = list(map(int, input().split()))

def max_consecutive_1s(arr:list) -> int:
    n = len(arr)
    max_1s = 0
    _1s = 0
    for i in range(n):
        if arr[i] == 1:
            _1s += 1
        else:
            _1s = 0
        max_1s = max(_1s,max_1s)
    
    return max_1s

print(max_consecutive_1s(arr))