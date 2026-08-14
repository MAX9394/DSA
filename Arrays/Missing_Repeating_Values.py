# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.
# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

def func(arr:list) -> list:
    unorderedSet = set([])
    n = len(arr)
    actualSum = 0
    for i in range(i):
        for j in range(j):
            actualSum += arr[i][j]
            if arr[i][j] in unorderedSet:
                a = arr[i][j]
            unorderedSet.add(arr[i][j])
    
    expSum = (n**2) * (n**2 + 1) // 2

    b = expSum + a - actualSum
    return [a,b]