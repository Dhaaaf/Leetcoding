# Write a function, is_binary_search_tree, that takes in the root of a binary tree. The function should return a boolean indicating whether or not the tree satisfies the binary search tree property.

# A Binary Search Tree is a binary tree where all values within a node's left subtree are smaller than the node's value and all values in a node's right subtree are greater than or equal to the node's value.




def is_binary_search_tree(root):
  values = []
  in_order_traversal(root, values)
  return is_sorted(values)

def in_order_traversal(root, values):
  if root is None:
    return
  in_order_traversal(root.left, values)
  values.append(root.val)
  in_order_traversal(root.right, values)

def is_sorted(numbers):
  for i in range(0, len(numbers) - 1):
    current = numbers[i]
    next = numbers[i+1]
    
    if next < current:
      return False
  return True