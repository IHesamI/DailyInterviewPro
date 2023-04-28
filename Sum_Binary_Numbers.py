def sum_binary(bin1, bin2):
    i = -1
    x = 0
    maxlen = len(bin1) if len(bin1) > len(bin2) else len(bin2)
    last_sum = 0
    final_num = []
    while True:

        try:
            num1 = int(bin1[i])
        except Exception:
            num1 = 0
        try:
            num2 = int(bin2[i])
        except Exception:
            num2 = 0
        sumed_num = num1+num2+last_sum
        last_sum = sumed_num//2
        added_num = sumed_num % 2
        final_num.append(str(added_num))
        i -= 1
        if x == maxlen-1:
            break
        x += 1
    if last_sum!=0:
        final_num.append('1')
    return ''.join(list(reversed(final_num)))


print(sum_binary("11101", "1011"))
# 101000
