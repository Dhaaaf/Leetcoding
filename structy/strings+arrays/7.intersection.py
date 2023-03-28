# Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

# You may assume that each input list does not contain duplicate elements.


# My solution + Alvin's including brute force:

def intersection(a, b):
  # result = []
  # for i in a:
  #   if i in b:
  #     result.append(i)
  # return result
  
  set_a = set(a)
  return [item for item in b if item in set_a]
