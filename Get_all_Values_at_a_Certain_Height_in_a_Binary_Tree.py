class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def valuesAtHeight(root, height):
    list_on_nodes=[]
    iterate_tree(root,height,list_on_nodes,1)
    return list_on_nodes

def iterate_tree(node,height,list:list,level=1):
    if level ==height:
        list.append(node.value)
    else:
        if node.left:
            iterate_tree(node.left,height,list,level+1)
        if node.right:
            iterate_tree(node.right,height,list,level+1)

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(valuesAtHeight(a, 3))
# [4, 5, 7]