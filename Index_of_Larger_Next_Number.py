def larger_number(nums):
    list_of_indexes=[]
    for i in range(len(nums)):
        index=-1
        for k in range(i+1,len(nums)):
            if nums[i]<nums[k]:
                index=k
                break
        list_of_indexes.append(index)
    return list_of_indexes
        
print(larger_number([3, 2, 5, 6, 9, 8]))
# print [2, 2, 3, 4, -1, -1]