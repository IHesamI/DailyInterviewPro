class Solution(object):
  # Fill this in.
  def addDigits(self,num):
      number=num
      while number>=10:
          rem=0
          divisionNumb=number
          sum=0
          while divisionNumb!=0:
              rem=divisionNumb%10
              divisionNumb//=10
              sum+=rem
          number=sum
      return number

print(Solution().addDigits(159))
# 1 + 5 + 9 = 15
# 1 + 5 = 6
# 6
