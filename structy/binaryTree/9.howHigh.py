# Write a function, how_high, that takes in the root of a binary tree. The function should return a number representing the height of the tree.

# The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.

# If the tree is empty, return -1.


# My recursive solution:
def how_high(node):
  if not node:
    return -1
  return 1 + max(how_high(node.left), how_high(node.right))

# Alvin's recursive solution:
def how_high(node):
  if node is None:
    return -1

  left_height = how_high(node.left)
  right_height = how_high(node.right)
  return 1 + max(left_height, right_height)
