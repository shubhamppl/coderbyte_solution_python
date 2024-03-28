'''// have the function PowerSetCount(arr) take the array of integers stored in arr, 
and return the length of the power set (the number of all possible sets) that can be generated. 
For example: if arr is [1, 2, 3], then the following sets form the power set: 
'''
def PowerSetCount(arr):
    # The size of the power set is 2 raised to the number of elements in the input array
    return 2 ** len(arr)

# Example usage
print(PowerSetCount([1,2, 23]))  # Expected output: 8
