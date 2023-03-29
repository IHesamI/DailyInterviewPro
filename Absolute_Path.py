def shortest_path(file_path):
    paths_stack=[]
    directories=list(filter(lambda x : x!='',file_path.split('/')))
    for dir in directories:
            if dir == '..':
                paths_stack.pop()
            elif dir != '..' and dir!='.':
                paths_stack.append(dir)
    path='/'+'/'.join(paths_stack)+'/'
    return path

print(shortest_path('/Users/Joma/Documents/../Desktop/./../'))
# /Users/Joma/