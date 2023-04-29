
def reverse_polish_notation(expr:list):
    index =0
    while True:
        for i in range(len(expr)):
            if expr[i]=='+':
                right_num=expr[i-1]
                left_num=expr[i-2]
                expr[i-2]=left_num+right_num
                expr.pop(i)
                expr.pop(i-1)
                break
            elif expr[i]=='-':
                right_num=expr[i-1]
                left_num=expr[i-2]
                expr[i-2]=left_num-right_num
                expr.pop(i)
                expr.pop(i-1)
                break
            
            elif expr[i]=='*':
                right_num=expr[i-1]
                left_num=expr[i-2]
                expr[i-2]=left_num*right_num
                expr.pop(i)
                expr.pop(i-1)
                break
            
            elif expr[i]=='/':
                right_num=expr[i-1]
                left_num=expr[i-2]
                expr[i-2]=left_num/right_num
                expr.pop(i)
                expr.pop(i-1)
                break
        if len(expr)==1:
            break
    return expr[0]
                

# 1 - (2 + 3) * 2
print(reverse_polish_notation([1, 2, 3, '+', 2, '*', '-']))
# -9