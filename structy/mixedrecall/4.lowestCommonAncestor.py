# Write a function, lowest_common_ancestor, that takes in the root of a binary tree and two values. The function should return the value of the lowest common ancestor of the two values in the tree.

# You may assume that the tree values are unique and the tree is non-empty.

# Note that a node may be considered an ancestor of itself.



# Alvin's recursice depth first solution
def lowest_common_ancestor(root, val1, val2):
  path1 = find_path(root, val1)
  path2 = find_path(root, val2)
  set2 = set(path2)
  
  for val in path1:
    if val in set2:
      return val

def find_path(root, target_val):
  if root is None:
    return None
  
  if root.val == target_val:
    return [ root.val ]
  
  left_path = find_path(root.left, target_val)
  if left_path is not None:
    left_path.append(root.val)
    return left_path
  
  right_path = find_path(root.right, target_val)
  if right_path is not None:
    right_path.append(root.val)
    return right_path
  
  return None
