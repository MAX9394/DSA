# A = [1,1,2,2,2,3,3]
A = list(map(int, input().split()))

def remove_duplicates(arr:list) -> list:
    return list(set(arr))

print(remove_duplicates(A))