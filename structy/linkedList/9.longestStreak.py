# Write a function, longest_streak, that takes in the head of a linked list as an argument. The function should return the length of the longest consecutive streak of the same value within the list.

# My iterative solution:

def longest_streak(head):
  long_streak = 0
  streak = 0
  val = 0
  while head:
    if val != head.val:
      streak = 0
      val = head.val
    if head.val == val:
      streak +=1
    if streak > long_streak:
      long_streak = streak
    head = head.next
  return long_streak

# Alvin's solution:

def longest_streak(head):
  max_streak = 0
  current_streak = 0
  prev_val = None
  
  current_node = head
  while current_node is not None:
    if current_node.val == prev_val:
      current_streak += 1
    else:
      current_streak = 1
  
    prev_val = current_node.val
    if current_streak > max_streak:
      max_streak = current_streak
    
    current_node = current_node.next
    
  return max_streak
