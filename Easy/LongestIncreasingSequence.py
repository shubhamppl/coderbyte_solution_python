'''// have the function LongestIncreasingSequence(arr) take the array of positive integers stored in arr and return 
the length of the longest increasing subsequence (LIS). A LIS is a subset of the original list where the numbers
are in sorted order, from lowest to highest, and are in increasing order. The sequence does not need to be contiguous or
unique, and there can be several different subsequences. For example: if arr is [4, 3, 5, 1, 6] then a possible
LIS is[3, 5, 6], and another is[1, 6].For this input, your program should return 3 because that is the length of
the longest increasing subsequence. '''

def LongestIncreasingSequence(arr):
    if not arr:
        return 0
    dp=[1]*len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)
print(LongestIncreasingSequence([4, 3, 5, 1, 6]))  # Output: 3
