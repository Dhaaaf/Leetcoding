# Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.


# My iterative depth first solution:
def tree_includes(root, target):
  if not root:
    return False
  
  stack = [root]
  while stack:
    current = stack.pop()
    if current.val == target:
      return True
    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)
  return False

# Alvin's recursive depth first solution:
def tree_includes(root, target):
  if not root:
    return False
  
  if root.val == target:
    return True
  
  return tree_includes(root.left, target) or tree_includes(root.right, target)


# Alvin's breath first solution:
from collections import deque

def tree_includes(root, target):
  if not root:
    return False
  
  queue = deque([ root ])
  
  while queue:
    node = queue.popleft()
    
    if node.val == target:
      return True
    
    if node.left:
      queue.append(node.left)
      
    if node.right:
      queue.append(node.right)
      
  return False
