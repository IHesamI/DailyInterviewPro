def check(lst):
    counter=0
    for i in range(len(lst)-1,0,-1):
        if lst[i]<lst[i-1]:
            counter+=1
    return True if counter==1 or counter==0 else False
        

print(check([13, 4, 7]))
# True
print(check([5,1,3,2,5]))
# False
