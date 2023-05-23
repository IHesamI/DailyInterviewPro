def one_bits(num):
    # Fill this in.
    counter=0
    while num > 0:
        rem = num % 2
        if rem==1:
            counter+=1
        num = num//2
    return counter


print(one_bits(23))
# 4
# 23 = 0b10111
