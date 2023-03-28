# Write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return a tuple containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair that sums to the target.

# My Solution:

def pair_sum(numbers, target_sum):
  nums = {}
  
  for index, num in enumerate(numbers):
    target = target_sum - num
    
    if target in nums:
      return (index, nums[target])
    
    nums[num] = index


# Alvin Solution:

def pair_sum(numbers, target_sum):
  previous_numbers = {}
  
  for index, num in enumerate(numbers):
    complement = target_sum - num
    
    if complement in previous_numbers:
      return (index, previous_numbers[complement])
    
    previous_numbers[num] = index
