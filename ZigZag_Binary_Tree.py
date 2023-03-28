class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return self.value


def zigzag_order(tree):
    pushed_nodes_stack = []
    nodes_and_levels_dict = {}
    level = 0
    nodes_and_levels_dict[0] = [tree]
    list_of_nodes = nodes_and_levels_dict[level]
    while True:
        try:
            for x in list_of_nodes:
                pushed_nodes_stack.append(x.value)
                try:
                    if level % 2 == 0:
                        inc_level = level+1
                        if inc_level not in nodes_and_levels_dict.keys():
                            nodes_and_levels_dict[inc_level] = []
                        if x.left:
                            nodes_and_levels_dict[inc_level].append(x.left)
                        if x.right:
                            nodes_and_levels_dict[inc_level].append(x.right)
                    else:
                        inc_level = level+1
                        if inc_level not in nodes_and_levels_dict.keys():
                            nodes_and_levels_dict[inc_level] = []
                        if x.right:
                            nodes_and_levels_dict[inc_level].append(x.right)
                        if x.left:
                            nodes_and_levels_dict[inc_level].append(x.left)
                except Exception:
                    continue
            level += 1
            list_of_nodes = nodes_and_levels_dict[level][::-1]

        except Exception:
            break
    print(nodes_and_levels_dict)
    return pushed_nodes_stack


n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)

print(zigzag_order(n1))
# [1, 3, 2, 4, 5, 6, 7]
