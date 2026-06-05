# arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arr2 = [2, 3, 4, 4, 5, 11, 12]
arr1 = list(map(int, input().split()))
# print(arr1)
arr2 = list(map(int, input().split()))
# print(arr2)

def union_set(arr1:list, arr2:list):
    return sorted(set(arr1)|set(arr2))

def union_map(arr1:list, arr2:list):
    n,m = len(arr1), len(arr2)
    freq = {}
    for i in range(n):
        freq[arr1[i]] = freq.get(arr1[i], 0) + 1 
    for j in range(m):
        freq[arr2[j]] = freq.get(arr2[j], 0) + 1
    
    union = sorted(freq.keys())

    return union

def union_optimal(arr1:list, arr2:list) -> list:
    n,m,i,j,res = len(arr1),len(arr2),0,0,[]
    
    while i < n and j < m:
        if arr1[i] < arr2[j] and arr1[i] not in res:
            res.append(arr1[i])
            i = i + 1
        elif arr1[i] > arr2[j] and arr2[j] not in res:
            res.append(arr2[j])
            j = j + 1
        else:
            res.append(arr1[i])
            i , j = i + 1, j + 1
    
    while i < n:
        res.append(arr1[i])
        i += 1
    
    while j < m:
        res.append(arr2[j])
        j += 1
    
    return res

print(union_set(arr1,arr2))
print(union_map(arr1,arr2))
print(union_optimal(arr1, arr2))