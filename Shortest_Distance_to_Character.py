def shortest_dist(s:str, c):
  # Fill this in.
  list_of_index = [i for i in range(len(s)) if s[i]==c ]
  final=[]
  for j in range(len(s)):
      final.append(min(map(lambda x : abs(x-j),list_of_index)))
  return final

print(shortest_dist('helloworld', 'l'))
# [2, 1, 0, 0, 1, 2, 2, 1, 0, 1]
