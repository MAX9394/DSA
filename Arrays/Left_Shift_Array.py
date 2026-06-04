# A = [13,46,24,52,20,9]
A = list(map(int, input().split()))

def lshift_array(arr:list) -> list:
    # arr.append(arr.pop(0))
    key = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = key
    return arr

print(lshift_array(A))