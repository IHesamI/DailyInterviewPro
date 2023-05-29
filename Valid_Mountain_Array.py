class Solution(object):

    def is_Asccending(self, arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True

    def is_desccending(self, arr):
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                return False
        return True

    def validMountainArray(self, arr: list):
        if len(arr) % 2 == 0:
            return False
        half_index = int((len(arr)-1)/2)
        is_lower_half_valid = self.is_Asccending(arr[:half_index+1])
        is_upper_half_valid = self.is_desccending(arr[half_index:])
        return (is_lower_half_valid and is_upper_half_valid)


print(Solution().validMountainArray([1, 2, 3, 2, 1]))
# True

print(Solution().validMountainArray([1, 2, 3]))
# False
