# Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.

# My and Alvin's iterative solution:

def reverse_list(head):
  prev, current = None, head
  
  while current:
    next = current.next
    current.next = prev
    prev = current
    current = next
  return prev

# Alvin's recursive solution
def reverse_list(head, prev = None):
  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)
