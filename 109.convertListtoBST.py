# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
# height-balanced
#  binary search tree.


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Find the middle of the tree first
        # That is going to be the head
        # Recursively sort the left and right lists to also make BST
        
        def findMid(head):
            slow = head
            fast = head
            prev = None

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            prev.next = None
            return slow


            
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        mid = findMid(head)
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root
