def rotate_list(nums, k):
    for j in range(k):
        temp=nums[0]
        for i in range(1,len(nums)):
            nums[i-1]=nums[i]
        nums[-1]=temp

a=[1, 2, 3, 4, 5]
rotate_list(a, 2)
print(a)
# [3, 4, 5, 1, 2]
