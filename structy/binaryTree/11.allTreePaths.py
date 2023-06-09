# Write a function, all_tree_paths, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.

# The order within an individual path must start at the root and end at the leaf, but the relative order among paths in the outer list does not matter.

# You may assume that the input tree is non-empty.

# Mine and Alvin's solution:
def all_tree_paths(root):
  if root is None:
    return []
  
  if root.left is None and root.right is None:
    return [[root.val]]
  
  paths = []
  
  left_sub_paths = all_tree_paths(root.left)
  for sub_path in left_sub_paths:
    paths.append([root.val, *sub_path])
    
  right_sub_paths = all_tree_paths(root.right)
  for sub_path in right_sub_paths:
    paths.append([root.val, *sub_path])
  
  return paths
