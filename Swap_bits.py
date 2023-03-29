def swap_bits(num):
    list_num=list(bin(num)[2:])
    for i in range(len(list_num)-1):
        list_num[i],list_num[i+1]=list_num[i+1],list_num[i]
    Number='0b'+''.join(list_num[:])
    return int(Number,2)


print(f"0b{swap_bits(0b10101010101010101010101010101010):032b}")
# 0b01010101010101010101010101010101
