def base_2(n):
    rem=0
    digits=[]
    while n !=0:
        rem=n%2
        digits.append(str(rem))
        n=int(n/2)
    return ''.join(digits[::-1])

print(base_2(123))
# 1111011
