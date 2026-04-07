from collections import defaultdict 

def Frequency(arr, n):
        # Create a defaultdict to store frequency of each element
    freq_map = defaultdict(int)

        # Traverse the array and count frequencies
    for i in range(n):
        freq_map[arr[i]] += 1
    
    # for key, value in freq_map.items():
    #     print(key, value)

        # Traverse through the defaultdict and print frequencies
    max_f = 1
    min_f = 10**6
    for key, value in freq_map.items():
        if value < min_f:
            min_k = key
            min_f = value
        if value > max_f:
            max_k = key
            max_f = value
        
    print(max_k, min_k)

    # Input array
arr = [10, 5, 10, 15, 10, 5]
n = len(arr)

    # Call the function to count frequencies
Frequency(arr, n)