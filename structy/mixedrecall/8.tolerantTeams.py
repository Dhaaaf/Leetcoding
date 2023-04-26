# Write a function, tolerant_teams, that takes in a list of rivalries as an argument. A rivalry is a pair of people who should not be placed on the same team. The function should return a boolean indicating whether or not it is possible to separate people into two teams, without rivals being on the same team. The two teams formed do not have to be the same size.



def tolerant_teams(rivalries):
  graph = make_graph(rivalries)
  
  coloring = {}
  
  for node in graph:
    if node not in coloring:
      stack = [(node, False)]
      while stack:
        node, color = stack.pop()
        if node in coloring:
          if color != coloring[node]:
            return False
        else:
          coloring[node] = color
        
        for neighbor in graph[node]:
          if neighbor not in coloring:
            stack.append((neighbor, not color))
  return True

def make_graph(edges):
  graph = {}
  
  for edge in edges:
    a,b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
      
    graph[a].append(b)
    graph[b].append(a)
  
  return graph
