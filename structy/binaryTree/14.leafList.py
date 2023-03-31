# Write a function, leaf_list, that takes in the root of a binary tree and returns a list containing the values of all leaf nodes in left-to-right order.

def leaf_list(root):
  if root is None:
    return []
  stack = [root]
  res = []
  while stack:
    current = stack.pop()
    
    if current.left is None and current.right is None:
      res.append(current.val)
    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)
    
  return res
