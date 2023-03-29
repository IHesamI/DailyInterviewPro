class Solution():  
  def fibonacci(self, n):
    fibo=[]
    fibo.append(0)
    fibo.append(1)
    for i in range(2,n+1):
        fibo.append(fibo[i-1]+fibo[i-2])
    return fibo[n]

n = 9
print(Solution().fibonacci(n))
# 34

