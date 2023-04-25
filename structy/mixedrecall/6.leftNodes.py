# Write a function, lefty_nodes, that takes in the root of a binary tree. The function should return a list containing the left-most value on every level of the tree. The list must be ordered in a top-down fashion where the root is the first item.

# Note that the left-most node on a level may not necessarily be a left child.



from collections import deque

def lefty_nodes(root):
  if root is None:
    return []
  
  values = []
  queue = deque([(root, 0)])
  
  while queue:
    node, level = queue.popleft()
    
    if level == len(values):
      values.append(node.val)
      
    if node.left:
      queue.append((node.left, level + 1))
    
    if node.right:
      queue.append((node.right, level + 1))
  
  return values
