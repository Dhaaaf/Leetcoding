# Write a function, linked_palindrome, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list is a palindrome. A palindrome is a sequence that is the same both forwards and backwards.


# My solution:def linked_palindrome(head):

def linked_palindrome(head):
  curr = head
  one = []
  while curr:
    one.append(curr.val)
    curr = curr.next
    
  current, prev = head, None
  while current:
    temp = current.next
    current.next = prev
    prev = current
    current = temp
    
  two = []
  while prev:
    two.append(prev.val)
    prev = prev.next
  
  return one == two

# Alvin's solution:
def linked_palindrome(head):
  values = []
  
  current = head
  while current is not None:
    values.append(current.val)
    current = current.next
    
  return values == values[::-1]
