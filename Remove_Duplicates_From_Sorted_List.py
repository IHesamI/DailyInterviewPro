def remove_dups(nums: list):
    # Fill this in.
    count = 0
    for i in range(len(nums)):
        try:
            if nums[i] != nums[i+1]:
                count += 1
        except Exception:
            count += 1

    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                j += 1
        i += 1

    return count


nums = [1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 9]
print(remove_dups(nums))
# 8
print(nums)
# [1, 2, 3, 4, 5, 6, 7, 9]

nums = [1, 1, 1, 1, 1, 1]
print(remove_dups(nums))
print(nums)
# 1
# [1]
