def to_bits(n):
    return '{0:032b}'.format(n)


def reverse_num_bits(num):
    number = to_bits(num)
    power = 0
    decimal_num = 0
    for digit in number:
        decimal_num = decimal_num + int(digit)*2**power
        power += 1
    return decimal_num


print(to_bits(1234))
# 00000000000000000000010011010010
print(reverse_num_bits(1234))
# 1260388352
print(to_bits(reverse_num_bits(1234)))
# 1001011001000000000000000000000
