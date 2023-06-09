# Write a function, middle_value, that takes in the head of a linked list as an argument. The function should return the value of the middle node in the linked list. If the linked list has an even number of nodes, then return the value of the second middle node.

# You may assume that the input list is non-empty.


def middle_value(head):
  slow, fast = head, head
  
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
  return slow.val
