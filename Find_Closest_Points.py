def closest_points(points, k):
    distances=[]
    for index,point in enumerate(points):
        distances.append(tuple((index,((point[0]**2)+(point[1]**2)))))
    sorted_distance=sorted(distances,key=lambda x : x[1])
    return_list=[]
    for i in range(k):
        return_list.append(points[sorted_distance[i][0]])
    return return_list
    
print(closest_points([(1, 2),(0, 0),  (-3, 4), (3, 1)], 2))
# [(1, 2), (0, 0)]