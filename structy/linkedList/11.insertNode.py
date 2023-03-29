# Write a function, insert_node, that takes in the head of a linked list, a value, and an index. The function should insert a new node with the value into the list at the specified index. Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

# Do this in-place.

# You may assume that the input list is non-empty and the index is not greater than the length of the input list.

# My solution:
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):
  new = Node(value)
  if index == 0:
    new.next = head
    return new
  i = 0
  current = head
  while i < index - 1 :
    current = current.next
    i +=1
  new.next = current.next
  current.next = new
  return head

# Alvin's iterative solution:
def insert_node(head, value, index):
  if index == 0:
    new_head = Node(value)
    new_head.next = head
    return new_head
    
  count = 0
  current = head
  while current is not None:
    if count == index - 1:
      temp = current.next
      current.next = Node(value)
      current.next.next = temp
    
    count += 1
    current = current.next
  return head

# Alvin's recursive solution:
def insert_node(head, value, index, count = 0):
  if index == 0:
    new_head = Node(value)
    new_head.next = head
    return new_head
  
  if head is None:
    return None
  
  if count == index - 1:
      temp = head.next
      head.next = Node(value)
      head.next.next = temp
      return 
  
  insert_node(head.next, value, index, count + 1)
  return head
