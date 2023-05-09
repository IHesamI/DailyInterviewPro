def majority_element(nums):
    # Fill this in.
    sorted_nums = sorted(nums)
    counter = 0
    majority_num=0
    
    for i in range(len(sorted_nums)):
        try:
            if sorted_nums[i] == sorted_nums[i+1]:
                counter += 1
            else:
                counter +=1
                if counter >= (len(sorted_nums)/2):
                    majority_num = sorted_nums[i]
                counter = 0
        except Exception:
                counter = +1
                if counter > len(sorted_nums)//2:
                    majority_num = sorted_nums[i]
                break     
    return majority_num


print(majority_element([3, 5, 3, 3, 2, 4, 3]))
# 3
