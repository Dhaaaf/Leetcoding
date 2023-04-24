# Write a function, flip_tree, that takes in the root of a binary tree. The function should flip the binary tree, turning left subtrees into right subtrees and vice-versa. This flipping should occur in-place by modifying the original tree. The function should return the root of the tree.

# My iterative solution:
def flip_tree(root):
  if root is None:
    return None
  stack = [root]
  while stack:
    node = stack.pop()
    node.right, node.left = node.left, node.right
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)
  return root

# Alvin's recursive solution:
def flip_tree(root):
  if root is None:
    return None
  left = flip_tree(root.left)
  right = flip_tree(root.right)  
  root.left = right
  root.right = left
  return root
