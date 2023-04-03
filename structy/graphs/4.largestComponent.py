# Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph.

# My iterative solution:
def largest_component(graph):
  size = 0
  visited = set()
  
  for node in graph:
    if node not in visited:
      stack = [node]
    
      count = 0
      while stack:
        current = stack.pop()
        if current not in visited: 
          count += 1
          visited.add(current)
          stack.extend([neighbor for neighbor in graph[current] if neighbor not in visited])

      size = max(size, count)
  return size

# Same solution woth helper function:
def largest_component(graph):
    visited = set()
    
    largest = 0
    for node in graph:
        size = explore_size(graph, node, visited)
        if size > largest:
            largest = size
    
    return largest

def explore_size(graph, node, visited):
    if node in visited:
        return 0

    stack = [node]
    size = 0

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            size += 1
            stack.extend(graph[current])

    return size

# Alvin's recursive solution:
def largest_component(graph):
  visited = set()
  
  largest = 0
  for node in graph:
    size = explore_size(graph, node, visited)
    if size > largest:
      largest = size
  
  return largest

def explore_size(graph, node, visited):
  if node in visited:
    return 0
  
  visited.add(node)
  
  size = 1
  for neighbor in graph[node]:
    size += explore_size(graph, neighbor, visited)
    
  return size
