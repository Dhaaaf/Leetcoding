# Write a function, can_color, that takes in a dictionary representing the adjacency list of an undirected graph. The function should return a boolean indicating whether or not it is possible to color nodes of the graph using two colors in such a way that adjacent nodes are always different colors.


# My iterative solutino:
def can_color(graph):
  coloring = {}
  for node in graph:
    if node not in coloring:
      stack = [(node, False)]
      while stack:
        current_node, current_color = stack.pop()
        if current_node in coloring:
          if current_color != coloring[current_node]:
            return False
        else:
            coloring[current_node] = current_color
            for neighbor in graph[current_node]:
              stack.append((neighbor, not current_color))
  return True



# Alvin's recurive solution
def can_color(graph):
  coloring = {}
  for node in graph:
    if node not in coloring:
      if not valid(graph, node, coloring, False):
        return False
  return True

def valid(graph, node, coloring, current_color):
  if node in coloring:
    return current_color == coloring[node]
  
  coloring[node] = current_color
  
  for neighbor in graph[node]:
    if not valid(graph, neighbor, coloring, not current_color):
      return False
  return True
