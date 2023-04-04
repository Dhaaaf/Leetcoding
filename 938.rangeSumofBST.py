# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        # nodes to the left are less than, nodes to thr right are greater than
        sum = 0

        stack = [root]
        while stack:
            current = stack.pop()
            if current.val >= low and current.val <= high:
                sum += current.val
            if current.right and current.val < high:
                stack.append(current.right)
            if current.left and current.val > low:
                stack.append(current.left)
        return sum
