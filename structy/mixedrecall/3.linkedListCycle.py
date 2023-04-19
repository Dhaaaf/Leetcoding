# linked list cycle
# Write a function, linked_list_cycle, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains a cycle.


# My solution:
def linked_list_cycle(head):
  if head == None:
    return False
  slow, fast = head, head.next
  
  while fast and fast.next:
    if slow == fast or fast.next == slow:
      return True
    slow = slow.next
    fast = fast.next.next
  return False

# Alvin's solution:
def linked_list_cycle(head):
  first_iteration = True
  
  fast = head
  slow = head
  while fast is not None and fast.next is not None:
    if slow is fast and not first_iteration:
      return True
    first_iteration = False
    slow = slow.next
    fast = fast.next.next
    
  return False
