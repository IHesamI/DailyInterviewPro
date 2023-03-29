def is_palindrome(n):
    revnumber=0
    temp=n
    while temp >0:
        rem=int(temp%10)
        revnumber=revnumber*10 + rem
        temp=int(temp/10)
    return n==revnumber
    

print(is_palindrome(1234321))
# True
print(is_palindrome(1234322))
# False