# You are given an array of prices where prices[i] is the price of a given stock on an ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# arr = [7,1,5,3,6,4]
arr = list(map(int, input().split(",")))

def func(arr:list) -> int:
    low = (2**31) - 1
    high = 0
    for i in arr:
        if i < low:
            low = i
            high = i
        high = max(high, i)

    return high - low

def func2(arr:list) -> int:
    '''Optimal code given in blog'''
    profit = 0
    low = float('inf')
    for i in arr:
        if i < low:
            low = i
        else:
            profit = max(profit, i - low)
    return profit

print(func(arr))