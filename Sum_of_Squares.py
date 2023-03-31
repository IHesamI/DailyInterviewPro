def find_counter(list_of_counters, number, index):
    i = index
    sum = number
    count = 0
    while True:
        index_num = list_of_counters[i]
        if sum-index_num**2 < 0:
            i -= 1
        else:
            sum -= (index_num**2)
            count += 1
            if sum == 0:
                break
    return count


def square_sum(n):
    list_of_numbers = []
    for x in range(1, int(n/2)):
        if x**2 > n:
            break
        list_of_numbers.append(x)
    # print(list_of_numbers)
    index = n
    for i in range(len(list_of_numbers)-1, -1, -1):
        new_index = find_counter(list_of_numbers, n, i)
        if new_index < index:
            index = new_index
    return index


print(square_sum(13))
# Min sum is 3**2 + 2**2
# 2

# print(square_sum(76))
# # Min sum is 6**2 +6**2 + 2**2
# # 3
