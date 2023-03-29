class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def __str__(self):
        level = 0
        values_and_levels_dict = {}
        nodes_and_levels_dict = {}
        nodes_and_levels_dict[0] = [tree]
        values_and_levels_dict[0] = []
        list_of_nodes = nodes_and_levels_dict[level]
        while True:
            try:
                for x in list_of_nodes:
                    values_and_levels_dict[level].append(x.value)
                    try:
                        inc_level = level+1
                        if inc_level not in nodes_and_levels_dict.keys():
                            nodes_and_levels_dict[inc_level] = []
                            values_and_levels_dict[inc_level] = []
                        if x.left:
                            nodes_and_levels_dict[inc_level].append(x.left)
                            
                        if x.right:
                            nodes_and_levels_dict[inc_level].append(
                                x.right)
                    except Exception:
                        continue
                level += 1
                list_of_nodes = nodes_and_levels_dict[level]
            except Exception:
                break
        nodes_in_which_level=[]
        for eachlevel in list(values_and_levels_dict.values()):
            if eachlevel:
                nodes_in_which_level.append(''.join(eachlevel))
        nodes_string='\n'.join(nodes_in_which_level)
        return nodes_string

tree = Node('a')
tree.left = Node('b')
tree.right = Node('c')
tree.left.left = Node('d')
tree.left.right = Node('e')
tree.right.left = Node('f')
tree.right.right = Node('g')

print(tree)
# a
# bc
# defg
