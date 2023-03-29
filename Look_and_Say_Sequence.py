def findNthSequence(n):
    k=0
    first_num = '1'
    value = first_num
    while k <n:
        prev_rem=value[0]
        i=0
        count=0
        new_val=''
        while i < len(value):
            rem=value[i]
            if prev_rem!=rem:
                new_val=new_val+str(count)+str(prev_rem)
                count=1
                prev_rem=rem
            else:
                count+=1
            i+=1
            if i==len(value):
                new_val=new_val+str(count)+str(rem)
        value=new_val
        k+=1     
    return new_val

print(findNthSequence(4))
# 111221