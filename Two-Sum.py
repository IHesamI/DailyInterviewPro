def two_sum(list, k):
    diff_set=set()
    for x in list:
        if (k-x) in diff_set:
            return True
        diff_set.add(x)
    return False

print(two_sum([4,7,1,-3,2], 5))
# True
