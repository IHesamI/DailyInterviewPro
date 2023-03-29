# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None
  def __str__(self) -> str:
      thenext=self.next
      string=str(self.value)
      while thenext:
        string+=str(thenext.value)
        thenext=thenext.next
      return string

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    origin= ListNode(0)
    result =origin    
    while l1:
      val1=l1.value
      val2=l2.value
      result.value=val1+val2+c
      if result.value % 10 == 0:
          c+=1
          result.value=0
          l1=l1.next
          if not l1:
            break
          result.next=ListNode(0)
          l2=l2.next
          result = result.next
          continue
      l1=l1.next
      if not l1:
        break
      result.next=ListNode(0)
      l2=l2.next
      result = result.next
      c=0
    
    return origin
            
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
# print(result)
while result:
  print(result.value)
  result = result.next
# 7 0 8
