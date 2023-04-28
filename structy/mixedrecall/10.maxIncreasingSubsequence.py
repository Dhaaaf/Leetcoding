# Write a function, max_increasing_subseq, that takes in a list of numbers as an argument. The function should return the length of the longest subsequence of strictly increasing numbers.

# A subsequence of a list can be created by deleting any items of the list, while maintaining the relative order of items.

def max_increasing_subseq(numbers):
  return _max_increasing_subseq(numbers, 0, float('-inf'), {})
  
def _max_increasing_subseq(numbers, i, previous, memo):
  key = (i, previous)
  
  if key in memo:
    return memo[key]
  
  if i == len(numbers):
    return 0
  
  current = numbers[i]
  options = []
  dont_take_current = _max_increasing_subseq(numbers, i + 1, previous, memo)
  options.append(dont_take_current)
  
  if current > previous:
    take_current = 1 + _max_increasing_subseq(numbers, i + 1, current, memo)
    options.append(take_current)
    
  memo[key] = max(options)
  return memo[key]
