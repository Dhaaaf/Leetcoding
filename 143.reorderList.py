# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # we have a linked list

        # return n0, last node, n1, 2nd last node, n2, third last node

        # By definition, our mid point will be the last node.

        # mid point .next = none

        # two pointer approach with a fast pointer, and a slow pointer

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        first = head
        curr, prev = mid, None

        # Reverse the 2nd half of the linked list
        while curr:
            # curr 3
            temp = curr.next  # temp 4
            curr.next = prev # 3 . next = None
            prev = curr # prev 3
            curr = temp # curr 4

        # 1 2 3 none
        # 4 5

        # 4.next = 3

        # 1 2 3 none

        # 4 3 none

        # 1 2 3 None

        # 5 4 3 None

        # Link first half with the corresponding 2nd half

        sec = prev

        while sec.next:
            temp2 = first.next
            temp3 = sec.next
            first.next = sec
            first = temp2

            sec.next = first
            sec = temp3