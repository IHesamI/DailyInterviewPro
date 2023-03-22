def square_numbers(nums):
    positive_lower_bound = 0
    negative_higher_bound = 0

    negative_array =[]
    negative_array_index=0
    sorted_array = []

    for i in range(len(nums)):
        if nums[i] >= 0:
            positive_lower_bound = i
            negative_higher_bound = i-1
            break
    for j in range(negative_higher_bound,-1,-1):
        negative_array.append(nums[j])        

    while True:
        try:
            neg_number = negative_array[negative_array_index]**2
            pos_number = nums[positive_lower_bound]**2

            if neg_number < pos_number:
                sorted_array.append(neg_number)
                negative_array_index += 1
            elif neg_number > pos_number :
                sorted_array.append(pos_number)
                positive_lower_bound += 1

            else:
                sorted_array.append(neg_number)
                negative_array_index += 1
                
                sorted_array.append(pos_number)
                positive_lower_bound += 1      
                
        except Exception:
            break
        
    if positive_lower_bound < len(nums):
        loopAppender(positive_lower_bound, len(nums), 1, sorted_array, nums)
    else:
        loopAppender(negative_higher_bound, 0, -1, sorted_array, nums)

    return sorted_array


def loopAppender(lowerbond, upperbond, step, sorted_array, nums):
    TheRange = range(lowerbond, upperbond, step) if step > 0 else range(
        upperbond, lowerbond, step)
    for i in TheRange:
        number = nums[i]**2
        sorted_array.append(number)


print(square_numbers([-5,-3,-2,0,1,4,5,5,7]))
# [0, 1, 4, 9, 16, 25, 25, 25, 49]
print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
# 0, 1, 1, 9, 16, 25, 25]