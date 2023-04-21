def frac_to_dec(numerator, denominator):
    result=str(numerator/denominator)
    index=0
    while True:
        if result[index]=='.':
            break
        index+=1
    number=list(result[:index])
    # return number
    while True:
        number.append(result[index])
        try:
            if result[index]==result[index+1]:
                number.pop()
                number.append('(')
                number.append(result[index])
                number.append(')')
                break
            if index+1==len(result):
                break
            index+=1
        except Exception:
            break
    
    return ''.join(number)
  

print(frac_to_dec(-3, 2))
# -1.5

print(frac_to_dec(4, 3))
# 1.(3)

print(frac_to_dec(1, 6))
# 0.1(6)


print(frac_to_dec(1, 8))
# 0.125
