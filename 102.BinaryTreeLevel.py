# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).




class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Bredth first search
        # Using a queue
        # When we're going through the tree, and adding to queue
        # Add the level of each node
        # return our result list

        if root is None:
            return []

        res = []
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            
            if len(res) == level:
                res.append([node.val])
            else:
                res[level].append(node.val)

            if node.left:
                queue.append((node.left, level +1))
            if node.right:
                queue.append((node.right, level +1))
        return res
