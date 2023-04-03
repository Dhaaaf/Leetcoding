# Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.


# My iterative depth first solution:
def connected_components_count(graph):
  visited = set()
  count = 0
  
  for node in graph:
    if node not in visited:
      stack = [node]
      
      while stack:
        current = stack.pop()
        
        visited.add(current)
        
        stack.extend([neighbor for neighbor in graph[current] if neighbor not in visited])
        
        # if current not in visited:
        #   visited.add(current)
        #   stack.extend([neighbor for neighbor in graph[current] if neighbor not in visited])
          
      count += 1
  return count

# Alvin's recursive solution:
def connected_components_count(graph):
  visited = set()
  count = 0
  
  for node in graph:
    if explore(graph, node, visited) == True:
      count += 1
      
  return count

def explore(graph, current, visited):
  if current in visited:
    return False
  
  visited.add(current)
  
  for neighbor in graph[current]:
    explore(graph, neighbor, visited)
  
  return True
