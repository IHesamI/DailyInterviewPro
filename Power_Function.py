def pow(x, n):
    if n==0:
        return 1
    elif n==1:
        return x
    else:
        if n%2==0:
            return pow(x*x,int(n/2))
        else :
            return x*pow(x*x,int(n/2))

print(pow(5,3))
# 125