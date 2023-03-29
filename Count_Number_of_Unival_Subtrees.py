class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_unival_subtrees(root: Node):
    sum = 0
    if root.left == None and root.right == None:
        return sum + 1
    elif root.right and root.left:
        if root.right.val == root.left.val == root.val:
            sum += 1
        sum += count_unival_subtrees(root.left)
        sum += count_unival_subtrees(root.right)
    elif root.right:
        sum += count_unival_subtrees(root.right)
    elif root.left:
        sum += count_unival_subtrees(root.left)
    return sum


a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(count_unival_subtrees(a))
# 5
