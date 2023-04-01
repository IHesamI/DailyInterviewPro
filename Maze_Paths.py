def iterate_maze_recursevly(maze, x_pos, y_pos, n, m):
    sum = 0

    if y_pos+1 < m and maze[x_pos][y_pos+1] != 1:
        sum += iterate_maze_recursevly(maze, x_pos, y_pos+1,n, m)
    if x_pos+1 < n and maze[x_pos+1][y_pos] != 1:
        sum += iterate_maze_recursevly(maze, x_pos+1, y_pos,n, m)
    elif  y_pos+1 == m and x_pos+1 == n:
        return 1
    return sum


def paths_through_maze(maze):
    return iterate_maze_recursevly(maze, 0, 0, len(maze), len(maze[0]))


print(paths_through_maze([[0, 1, 0],
                          [0, 0, 1],
                          [0, 0, 0]]))
# 2
