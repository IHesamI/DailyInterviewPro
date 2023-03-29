def find_continuous_k(list, k):
    sum = 0
    sub_index=0
    for i in range(len(list)):
        if sum < k :
            sum+=list[i]
        while sum > k and sub_index<i:
            sum-=list[sub_index]
            sub_index+=1
        if sum == k:
            return list[sub_index:i+1]
        
print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]
