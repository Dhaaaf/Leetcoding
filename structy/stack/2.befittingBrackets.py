# Write a function, befitting_brackets, that takes in a string as an argument. The function should return a boolean indicating whether or not the string contains correctly matched brackets.

# You may assume the string contains only characters: ( ) [ ] { }

def befitting_brackets(string):
  brackets = {"(" : ")", "[" : "]", "{" : "}"}
  stack = []
  
  for s in string:
    if s in brackets:
      stack.append(brackets[s])
    else:
      if stack and stack[-1] == s:
        stack.pop()
      else:
        return False
  
  return len(stack) == 0


# My older solution:
class Solution:
    def isValid(self, s: str) -> bool:
        # First opening bracket must be closed after all other opening brackets before it's own closing bracket.

        # Make our stack
        stack = []
        #Iterate through our string
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            elif not stack or char != stack.pop():
                return False

        return len(stack) == 0
