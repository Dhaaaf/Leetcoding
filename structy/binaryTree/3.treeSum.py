# Write a function, tree_sum, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree.

# My breath first solution:

from collections import deque

def tree_sum(root):
  if not root:
    return 0
  
  total = 0
  queue = deque([root])
  
  while queue:
    current = queue.popleft()
    total += current.val
    
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
  return total


# Alvin's recursive dpeth first solution
def tree_sum(root):
  if root is None:
    return 0
  return root.val + tree_sum(root.left) + tree_sum(root.right)
