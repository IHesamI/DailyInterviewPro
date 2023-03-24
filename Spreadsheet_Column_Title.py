class Solution:
  def convertToTitle(self, n):
    stack=[]
    string=''
    level=0
    while n !=0:
      reminder=n%26
      if reminder==0:
        n-= (26**level)
        reminder=26
      n=int(n/26)
      stack.append(reminder)
    length=len(stack)
    for x in range(length):
      ascii=chr(stack.pop()+64)
      string+=ascii
    return string
      


input1 = 1
input2 = 456976
input3 = 28
print(Solution().convertToTitle(input1))
# A
print(Solution().convertToTitle(input2))
# YYYZ
print(Solution().convertToTitle(input3))
# AB