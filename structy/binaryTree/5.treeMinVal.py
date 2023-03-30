



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
