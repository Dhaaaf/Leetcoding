# Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

# You can assume that the input string is non-empty.

def most_frequent_char(s):
  obj = {}
  for c in s:
    if c not in obj:
      obj[c]=0
    obj[c] +=1
    
  high = 0
  letter = ""
  for c in s:
    if obj[c] > high:
      high = obj[c]
      letter = c
      
  return letter
