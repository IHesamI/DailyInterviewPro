class Solution:
    def reverse(self, x):
        revNumber=0
        while x >0:
            rem=x%10
            revNumber=revNumber*10 +rem
            x=int(x/10)
        return 0 if revNumber>2**31 else revNumber
print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0