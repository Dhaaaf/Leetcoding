# Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.

# My and Alvin's iterative solution:

def sum_list(head):
  res = 0
  current = head
  while current is not None:
    res += current.val
    current = current.next
  return res

# Alvin's recursive solution:
def sum_list(head):
  if head is None:
    return 0
  return head.val + sum_list(head.next)
