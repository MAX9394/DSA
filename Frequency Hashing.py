# Count the number of occurences of each element in an array (positive integer array)

A = [10,5,10,15,10,5]

m = max(A)

X = [0] * (m+1)

for i in A:
    X[i] += 1

for j in range(m+1):
    if X[j] > 0:
        print(j, X[j])

# from collections import defaultdict

# # Function to count frequency of each element in the array using defaultdict
# def Frequency(self, arr, n):
#         # Create a defaultdict to store frequency of each element
#     freq_map = defaultdict(int)

#         # Traverse the array and count frequencies
#     for i in range(n):
#         freq_map[arr[i]] += 1

#         # Traverse through the defaultdict and print frequencies
#     for key, value in freq_map.items():
#         print(key, value)

#     # Input array
# arr = [10, 5, 10, 15, 10, 5]
# n = len(arr)

#     # Call the function to count frequencies
# Frequency(arr, n)
