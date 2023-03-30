# Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. The function should return the minimum value within the tree.

# You may assume that the input tree is non-empty.


# My breath first solution:


from collections import deque

def tree_min_value(root):
  min_val = root.val
  
  queue = deque([root])
  while queue:
    current = queue.popleft()
    if current.val < min_val:
      min_val = current.val
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
  return min_val
