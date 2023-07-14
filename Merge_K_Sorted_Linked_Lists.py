# TODO
#! very unconsistent and need to debug with more tests 
class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

def twoListMerge(list1:Node,list2:Node):
    final_list:Node=Node(None,None)
    root=final_list
    list1_cursor=list1
    list2_cursor=list2
    while(list1_cursor!=None and list2_cursor!=None ):
        # print(final_list,list2_cursor!=None)
        if list1_cursor!=None and list1_cursor.val>list2_cursor.val:
            final_list.val=list2_cursor.val
            final_list.next=Node(None,None)
            final_list=final_list.next
            list2_cursor=list2_cursor.next
        elif list2_cursor!=None and list1_cursor.val<list2_cursor.val:
            final_list.val=list1_cursor.val
            final_list.next=Node(None,None)
            final_list=final_list.next
            list1_cursor=list1_cursor.next
    return root
def merge(lists):
  # Fill this in.
    Merged_link_list=lists[0]
    merged_root=Merged_link_list
    for i in range(1,len(lists)):
        Merged_link_list=twoListMerge(Merged_link_list,lists[i])
        merged_root=Merged_link_list
    return merged_root

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))
# 123456