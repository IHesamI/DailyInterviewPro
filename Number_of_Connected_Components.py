def num_connected_components(edges):
    list_of_edges=[]

    for each_way in edges:
        if len(list_of_edges)==0:
            new_comp=set()
            new_comp.add(each_way[0])
            new_comp.add(each_way[1])
            list_of_edges.append(new_comp)
        else:
            for comp in list_of_edges:
                if each_way[0] in comp or each_way[1] in comp:
                    comp.add(each_way[0]) 
                    comp.add(each_way[1])
                else:
                    new_comp=set()
                    new_comp.add(each_way[0])
                    new_comp.add(each_way[1])
                    list_of_edges.append(new_comp)

    return list_of_edges

print(num_connected_components([(1, 2), (2, 3), (4, 1), (5, 6)]))
# 2