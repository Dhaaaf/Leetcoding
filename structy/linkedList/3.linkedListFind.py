# Write a function, linked_list_find, that takes in the head of a linked list and a target value. The function should return a boolean indicating whether or not the linked list contains the target.

# My and Alvin's iterative solution:
def linked_list_find(head, target):
  current = head
  while current is not None:
    if current.val is target:
      return True
    current = current.next
  return False

# Alvin's recursive solution:
def linked_list_find(head, target):
  if head is None:
    return False
  if head.val == target:
    return True
  return linked_list_find(head.next, target)
