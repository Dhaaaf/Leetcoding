# Write a function, remove_node, that takes in the head of a linked list and a target value as arguments. The function should delete the node containing the target value from the linked list and return the head of the resulting linked list. If the target appears multiple times in the linked list, only remove the first instance of the target in the list.

# Do this in-place.

# You may assume that the input list is non-empty.

# You may assume that the input list contains the target.

#My Solution:
def remove_node(head, target_val):
  if head.val == target_val:
    return head.next
  current = head
  while current.next.val != target_val:
    current = current.next
  current.next = current.next.next
  return head

# Alvin's iterative solution:
def remove_node(head, target_val):
  if head.val == target_val:
    return head.next

  current = head
  prev = None
  while current is not None:
    if current.val == target_val:
      prev.next = current.next
      break
    prev = current
    current = current.next
  return head

# Alvin's recursive solution:
def remove_node(head, target_val):
  if head is None:
    return None

  if head.val == target_val:
    return head.next

  head.next = remove_node(head.next, target_val)
  return head
