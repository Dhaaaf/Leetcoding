# Given the head of a singly linked list, reverse the list, and return the reversed list.



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev