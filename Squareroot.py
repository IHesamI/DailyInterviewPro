# Using Heron's Method https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
def sqrt(x):
    num=int(x)/2
    for i in range(100):
        try:
            num=(num+x/num)/2
        except Exception:
            return num
    return f'{num:.3f}'
  
print(sqrt(5))
# 2.236
