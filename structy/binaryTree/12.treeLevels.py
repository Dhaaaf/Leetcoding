# Write a function, tree_levels, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each sublist represents a level of the tree.

from collections import deque

def tree_levels(root):
  if root is None:
    return []
  
  levels = []
  
  queue = deque([(root, 0)])
  
  while queue:
    current, level_num = queue.popleft()
