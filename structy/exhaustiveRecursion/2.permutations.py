# Write a function, permutations, that takes in a list an argument. The function should return a 2D list where each sublist represents one of the possible permutations of the list.

# The sublists may be returned in any order.

# You may assume that the input list contains unique items.


def permutations(items):
  if not items:
    return [[]]
  
  item = items.pop()
  perms = permutations(items)
  result = []
  for perm in perms:
    for i in range(len(perm) + 1):
      result.append([*perm[:i], item, *perm[i:]])
      
  return result
