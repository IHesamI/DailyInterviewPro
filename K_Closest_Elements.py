def closest_nums(nums, k, x):
 map_of_dist_and_nums={num : abs(num-x) for num in nums }
 map_of_dist_and_nums=sorted(map_of_dist_and_nums.items(),key=lambda x :x[1])
 return [map_of_dist_and_nums[num][0] for num in range(k)]
 
print(closest_nums([1, 3, 7, 8, 9], 3, 5))
# [7, 3, 8]
