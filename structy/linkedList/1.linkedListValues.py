# Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

# Hey. This is our first linked list problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ

# My and Alvin's iterative solution

def linked_list_values(head):
  current = head
  res = []
  while current is not None:
    res.append(current.val)
    current = current.next
  return res


# Alvin's recursive solution

def linked_list_values(head):
  values = []
  _linked_list_values(head, values)
  return values

def _linked_list_values(head, values):
  if head is None:
    return
  values.append(head.val)
  _linked_list_values(head.next, values)
