# Write a function, paired_parentheses, that takes in a string as an argument. The function should return a boolean indicating whether or not the string has well-formed parentheses.

# You may assume the string contains only alphabetic characters, '(', or ')'.

# Stack solution:
def paired_parentheses(string):
  stack = []
  
  for s in string:
    if s == "(":
      stack.append(s)
    if s == ")":
      if len(stack) == 0:
        return False
      elif stack[-1] == "(":
        stack.pop()
  
  return len(stack) == 0


# Counter solution:
def paired_parentheses(string):
  count = 0
  
  for char in string:
    if char == '(':
      count += 1
    elif char == ')':
      if count == 0:
        return False
      count -= 1
      
  return count == 0
