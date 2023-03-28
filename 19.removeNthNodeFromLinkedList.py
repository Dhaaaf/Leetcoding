# Given the head of a linked list, remove the nth node from the end of the list and return its head.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two passes through the list
        # first just to get the length of the list
        # second to actually remove the node.

        # Double Pass solution

        # if head.next == None and n == 1:
        #     return None

        # length = 1
        # first_pass = head
        # while first_pass:
        #     first_pass = first_pass.next
        #     length += 1
        
        # #find node to replace
        # replace = length - n

        # # second pass though
        # i = head
        # counter = 1

        # while counter < replace - 1:
        #     i = i.next
        #     counter += 1

        # if replace == 1:
        #     head = head.next

        # i.next = i.next.next

        # return head


        # Single Pass Solution

        dummy = ListNode(0, head)

        left = dummy
        right = head

        sep = 0
        while sep < n:
            right = right.next
            sep +=1
        
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next
