# Write a function, post_order, that takes in the root of a binary tree. The function should return a list containing the post-ordered values of the tree.

# Post-order traversal is when nodes are recursively visited in the order: left child, right child, self.


# My Iterative Solution:
def post_order(root):
    if root is None:
        return []
    
    result = []
    stack = [(root, False)]
    
    while stack:
        node, visited = stack.pop()
        
        if node is None:
            continue
        
        if visited:
            result.append(node.val)
        else:
            # Push the node back into the stack with the visited flag set to True
            stack.append((node, True))
            
            # Push the right and left children into the stack
            stack.append((node.right, False))
            stack.append((node.left, False))
            
    return result


# Alvin's recursive post-order traversal
def post_order(root):
  values = []
  post_order_traversal(root, values)
  return values

def post_order_traversal(root, values):
  if root is None:
    return 
  post_order_traversal(root.left, values)
  post_order_traversal(root.right, values)
  values.append(root.val)