# Write a function, tree_value_count, that takes in the root of a binary tree and a target value. The function should return the number of times that the target occurs in the tree.

# My breath first solution:
from collections import deque

def tree_value_count(root, target):
  if not root:
    return 0
  count = 0
  queue = deque([root])
  
  while queue:
    curr = queue.popleft()
    if curr.val == target:
      count += 1
    if curr.left:
      queue.append(curr.left)
    if curr.right:
      queue.append(curr.right)
  return count

# Alvin's recursive solution:
def tree_value_count(root, target):
  if root is None:
    return 0

  match = 1 if root.val == target else 0

  return match + tree_value_count(root.left, target) + tree_value_count(root.right, target)
