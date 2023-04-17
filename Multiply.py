def sum_of_numbers(list_of_numbers:list[list],max_length:int):
    final_result = []
    rem=0
    for col in range(max_length):
        sum=0
        if rem!=0:
            sum+=rem
        for row in range(len(list_of_numbers)):
            try:
                sum+=list_of_numbers[row][-1-col]
            except Exception:
                continue
        if sum>=10:
            rem=int(sum/10)
            sum=sum%10
        else:
            rem=0

        final_result.append(str(sum))
    return ''.join(list(reversed(final_result)))          

def multiply(str1, str2):
    if len(str1) > len(str2):
        bigger = list(str1)
        lower = list(str2)
    else:
        bigger = list(str2)
        lower = list(str1)

    multiplied_numbers_list = []
    power = 0
    rem=0
    max_length=0
    for x in range(len(lower)-1, -1, -1):
        # print(x)
        p = power*[0]
        sub_list_of_mul = []
        rem=0
        for y in range(len(bigger)-1, -1, -1):
            result = int(bigger[y])*int(lower[x])
            # print(result)
            if rem!=0:
                result+=rem
                rem=0
            
            if result >= 10:
                rem = int(result/10)
                result %= 10
            else:
                rem = 0
            # print(result)
            sub_list_of_mul.append(result)
        
        if rem!=0:
            sub_list_of_mul.append(rem)
            
            
        sub_list_of_mul=list(reversed(sub_list_of_mul))
        sub_list_of_mul.extend(p)
        if len(sub_list_of_mul)>max_length:
            max_length=len(sub_list_of_mul)
        power += 1
        multiplied_numbers_list.append(sub_list_of_mul)
    
    return sum_of_numbers(multiplied_numbers_list,max_length)
print(multiply("123", "51"))
# 6273
