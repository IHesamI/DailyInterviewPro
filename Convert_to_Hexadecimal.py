def to_hex(n):
    list_of_numbers=[]
    rem=0

    while n !=0:
        rem =n%16
        if rem >=10:
            rem=chr(rem+55)
            list_of_numbers.append(rem)
        else:
            list_of_numbers.append(str(rem))
        n=int(n/16)

    return ''.join(reversed(list_of_numbers))
  
print(to_hex(123))
# 7B
