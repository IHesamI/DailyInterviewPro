class Solution:
    def getRange(self, arr, target):
        last_index = -1
        first_index = -1
        differ = -1
        for i in range(len(arr)):
            if arr[i] == target:
                last_index = i
                differ += 1
                first_index = last_index-differ
        return (first_index, last_index)


# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
# arr=[1,2,3,4,5,6,10]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
