def singleNumber(nums):
    number = 0
    for x in nums:
        number ^= x   
    return number

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1
