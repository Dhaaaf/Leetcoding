# Write a function, rare_routing, that takes in a number of cities (n) and a list of tuples where each tuple represents a direct road that connects a pair of cities. The function should return a boolean indicating whether or not there exists a unique route for every pair of cities. A route is a sequence of roads that does not visit a city more than once.

# Cities will be numbered 0 to n - 1.

# You can assume that all roads are two-way roads. This means if there is a road between A and B, then you can use that road to go from A to B or go from B to A.

# My iterative solution:
def rare_routing(n, roads):
    graph = make_graph(roads)
    visited = set()
    stack = [(0, None)]  # start_node, last_node

    while stack:
        node, last_node = stack.pop()

        if node in visited:
            return False

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor != last_node:
                stack.append((neighbor, node))

    return len(visited) == n

def make_graph(roads):
  graph = {}
  
  for road in roads:
    a, b = road
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    
    graph[a].append(b)
    graph[b].append(a)
  return graph


# Alvin's recursive solution:
def rare_routing(n, roads):
  graph = make_graph(n, roads)
  visited = set()
  valid = validate(graph, 0, visited, None)
  return valid and len(visited) == n


def validate(graph, node, visited, last_node):
  if node in visited:
    return False
  
  visited.add(node)
  for neighbor in graph[node]:
    if neighbor != last_node and not validate(graph, neighbor, visited, node):
      return False
    
  return True

def make_graph(n, roads):
  graph = {}
  
  for city in range(n):
    graph[city] = []
    
  for road in roads:
    a, b = road
    graph[a].append(b)
    graph[b].append(a)
    
  return graph
