# Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

# My Solution

def compress(s):
  s += "!"
  result = ""
  i = 0
  j = 0
  num = 0
  while j < len(s):
    if s[j] == s[i]:
      num +=1
      j +=1
      print("HERE", num)
    else:
      if num == 1:
        result += s[i]
        i = j
        num = 0
      else:
        result += str(num)
        result += s[i]
        i = j
        num = 0
  return result

# Alvin Solution

def compress(s):
  s += '!'
  result = []
  i = 0
  j = 0
  while j < len(s):
    if s[i] == s[j]:
      j += 1  
    else:
      num = j - i
      if num == 1:
        result.append(s[i])
      else:
        result.append(str(num)) 
        result.append(s[i])
      i = j
    
  return ''.join(result)