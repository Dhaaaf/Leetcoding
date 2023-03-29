# Write a function, is_univalue_list, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

# You may assume that the input list is non-empty.

# My iterative solutions:

def is_univalue_list(head):
  while head and head.next:
    if head.val == head.next.val:
      head = head.next
    else:
      return False
  return True

# Alvin's iterative solution:
def is_univalue_list(head):
  current = head
  while current is not None:
    if current.val != head.val:
      return False
    current = current.next
  return True

# Alvin's recursive solution:
def is_univalue_list(head, prev_val = None):
  if head is None:
    return True
  if prev_val is None or head.val == prev_val:
    return is_univalue_list(head.next, head.val)
  else:
    return False
