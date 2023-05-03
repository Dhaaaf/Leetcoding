# Write a function, binary_search_tree_includes, that takes in the root of a binary search tree containing numbers and a target value. The function should return a boolean indicating whether or not the target is found within the tree.

# A Binary Search Tree is a binary tree where all values within a node's left subtree are smaller than the node's value and all values in a node's right subtree are greater than or equal to the node's value.

# Your solution should have a best case runtime of O(log(n)).


# My iterative solution:

def binary_search_tree_includes(root, target):
  node = root
  while node:
    if target == node.val:
      return True
    if target < node.val:
      if node.left:
        node = node.left
      else:
        return False
    if target > node.val:
      if node.right:
        node = node.right
      else:
        return False
      
# Alvin's recursive solution:

def binary_search_tree_includes(root, target):
  if root is None:
    return False
  
  if root.val == target:
    return True
  
  if target < root.val:
    return binary_search_tree_includes(root.left, target)
  else:
    return binary_search_tree_includes(root.right, target)
