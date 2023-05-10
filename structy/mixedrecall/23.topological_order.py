# Write a function, topological_order, that takes in a dictionary representing the adjacency list for a directed-acyclic graph. The function should return a list containing the topological-order of the graph.

# The topological ordering of a graph is a sequence where "parent nodes" appear before their "children" within the sequence.




def topological_order(graph):
  num_parents = {}
  for node in graph:
    num_parents[node] = 0
  
  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1
      
  ready = [node for node in graph if num_parents[node] == 0]
  order = []
  while ready:
    node = ready.pop()
    order.append(node)
    for child in graph[node]:
      num_parents[child] -= 1
      if num_parents[child] == 0:
        ready.append(child)
  return order