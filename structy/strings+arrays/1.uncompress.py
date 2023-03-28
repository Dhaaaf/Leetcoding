# Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:


# The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.

# My Solution

def uncompress(s):
  numbers = '0123456789'
  i = 0
  j = 0
  result = ''
  while j < len(s):
    if s[j] in numbers:
      j +=1
    else:
      num = int(s[i:j])
      result += (s[j]*num)
      j+=1
      i = j
  return result


# Alvin Solution

def uncompress(s):
  numbers = '0123456789'
  result = []
  i = 0
  j = 0
  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:      
      num = int(s[i:j])
      result.append(s[j] * num)
      j += 1
      i = j
      
  return ''.join(result)
