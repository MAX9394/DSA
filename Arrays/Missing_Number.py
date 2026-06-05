# [8, 2, 4, 5, 3, 7, 1]
arr = list(map(int, input().split()))

def missing_number(arr:list) -> int:
    n = len(arr) + 1
    check_sum = int((n * (n + 1)) / 2)

    sum_arr = sum(arr)

    return check_sum - sum_arr

print(missing_number(arr))