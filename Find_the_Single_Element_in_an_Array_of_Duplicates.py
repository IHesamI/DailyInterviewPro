class Solution(object):
    def findSingle(self, nums):
        num = 0
        for number in nums:
            num ^= number  # Xor of two numbers return 0 when they are the same
            # and return non-zero number when one of them is 0 and the other is not
        return num
    
nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
# 3
