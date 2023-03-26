def findRange(nums):
    first_index = len(nums)
    last_index = 0
    for num in range(len(nums)):
        for afternum in range(num+1, len(nums)):
            if nums[num] > nums[afternum]:
                last_index = afternum
                if num < first_index:
                    first_index = num
    return (first_index, last_index)


print(findRange([1, 7, 9, 5, 7, 8, 10]))
# (1, 5)

print(findRange([1, 7, 9, 5, 7, 8, 0]))
# (0, 6)
