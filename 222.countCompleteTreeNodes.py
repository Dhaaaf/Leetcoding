# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.right == None and root.left == None:
            return 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    

# Correct solution:

def countNodes(root: TreeNode) -> int:
    if not root:
        return 0

    # Calculate the depth of the tree
    depth = 0
    node = root
    while node.left:
        depth += 1
        node = node.left

    # Binary search to find the number of nodes in the last level
    left, right = 0, 2 ** depth - 1
    node = root
    while left < right and node:
        mid = (left + right) // 2
        if (1 << (depth - 1)) & mid == 0:
            node = node.left
        else:
            node = node.right
        depth -= 1

        if not node:
            right = mid
        else:
            left = mid + 1

    # Total number of nodes = nodes in all levels except last + nodes in the last level
    return (2 ** depth - 1) + left
