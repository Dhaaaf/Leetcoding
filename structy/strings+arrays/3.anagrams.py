# Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

# My solution:

def anagrams(s1, s2):
  return to_dict(s1) == to_dict(s2)
  
def to_dict(string):
  obj = {}
  for s in string:
    if s not in obj:
      obj[s] = 1
    else:
      obj[s] +=1
  return obj

# Alvin's solution

def anagrams(s1, s2):
  return char_count(s1) == char_count(s2)

def char_count(s):
  count = {}
  
  for char in s:
    if char not in count:
      count[char] = 0
    count[char] += 1
  
  return count
