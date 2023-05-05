# Write a function, build_tree_in_pre, that takes in a list of in-ordered values and a list of pre-ordered values for a binary tree. The function should build a binary tree that has the given in-order and pre-order traversal structure. The function should return the root of this tree.

# You can assume that the values of inorder and preorder are unique.



class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_pre(in_order, pre_order):
  if len(in_order) == 0:
    return None
  value = pre_order[0]
  root = Node(value)
  mid = in_order.index(value)
  left_in = in_order[:mid]
  right_in = in_order[mid + 1:]
  left_pre = pre_order[1: 1 + len(left_in)]
  right_pre = pre_order[1 + len(left_in):]
  root.left = build_tree_in_pre(left_in, left_pre)
  root.right = build_tree_in_pre(right_in, right_pre)
  return root