# Write a function, create_linked_list, that takes in a list of values as an argument. The function should create a linked list containing each item of the list as the values of the nodes. The function should return the head of the linked list.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# My solution:

def create_linked_list(values):
  reversed = values.reverse()
  head = None
  for i in values:
    new = Node(i)
    new.next = head
    head = new
  return head

# Alvin's iterative solution:
def create_linked_list(values):
  dummy_head = Node(None)
  tail = dummy_head
  for val in values:
    tail.next = Node(val)
    tail = tail.next
  return dummy_head.next

# Alvin's recursive solution:
def create_linked_list(values, i = 0):
  if i == len(values):
    return None
  head = Node(values[i])
  head.next = create_linked_list(values, i + 1)
  return head
