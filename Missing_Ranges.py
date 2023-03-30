def missing_ranges(nums, low, high):
    miss_num = []
    TheRanges=[]
    for i in range(low, high):
        if i not in nums:
            miss_num.append(i)
    lowerindex=0
    higherindex=0
    counter=0
    for i in range(len(miss_num)):
        try:
            if miss_num[i]+1==miss_num[i+1]:
                counter+=1
            else:
                lowerindex=i
                higherindex=i
                TheRanges.append((miss_num[lowerindex-counter],miss_num[higherindex]))
                counter=0
        except Exception:
                lowerindex=i
                higherindex=i
                TheRanges.append((miss_num[lowerindex-counter],miss_num[higherindex]))
    return TheRanges


print(missing_ranges([1, 3, 5, 10], 1, 10))
# [(2, 2), (4, 4), (6, 9)]


# print(missing_ranges([2, 3, 5, 8], 1, 10))
# # [(1, 1), (4, 4), (6, 7),(9,9)]

# print(missing_ranges([1, 3, 5, 8], 1, 10))
# # [(2, 2), (4, 4),(6,7), (9, 9)]
