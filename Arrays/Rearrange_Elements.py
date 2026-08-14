# There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

# arr = [1,2,-4,-5]
arr = list(map(int, input().split(",")))
n = int(input())

def func(arr:list, n:int) -> list:
    i = 0
    res = []
    while i < n:
        res.append(arr[i])
        res.append(arr[n + i])
        i += 1
    return res

def func2(arr:list, n:int) -> list:
    res = [0] * n
    pos_i = 0
    neg_i = 1

    for i in range(n):
        if arr[i]<0:
            res[neg_i] = arr[i]
            neg_i += 2
        else:
            res[pos_i] = arr[i]
            pos_i += 2
    return res

print(func2(arr, n))