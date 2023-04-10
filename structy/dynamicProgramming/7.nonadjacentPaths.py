# Write a function, non_adjacent_sum, that takes in a list of numbers as an argument. The function should return the maximum sum of non-adjacent items in the list. There is no limit on how many items can be taken into the sum as long as they are not adjacent.

def non_adjacent_sum(nums):
  return _non_adjacent_sum(nums, 0, {})

def _non_adjacent_sum(nums, i, memo):
  if i in memo:
    return memo[i]
  
  if i >= len(nums):
    return 0
  
  include = nums[i] + _non_adjacent_sum(nums, i + 2, memo)
  exclude = _non_adjacent_sum(nums, i + 1, memo)
  memo[i] = max(include, exclude)
  return memo[i]
