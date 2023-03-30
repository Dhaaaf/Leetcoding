# Write a function, breadth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in breadth-first order.d


# My iterative solution: (O(n^2) because of the popping(0) from queue)

def breadth_first_values(root):
  if not root:
    return []
  
  queue = [root]
  values = []
  while queue:
    node = queue.pop(0)
    values.append(node.val)
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return values


#Alvin's iterative solution: O(n) because fo the Deque
from collections import deque

def breadth_first_values(root):
  if not root:
    return []
  
  queue = deque([ root ])
  values = []
  
  while queue:
    node = queue.popleft()
    
    values.append(node.val)
    
    if node.left:
      queue.append(node.left)
      
    if node.right:
      queue.append(node.right)
      
  return values
