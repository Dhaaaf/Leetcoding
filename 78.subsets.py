# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Iterative

def subsets(nums):
    res = [[]]
    for num in nums:
        for subset in res[:]:
            res.append(subset + [num])
    return res



# Recursive

def subsets(nums):
    if len(nums) == 0:
        return [[]]
    else:
        num = nums.pop()
        prev_subsets = subsets(nums)
        new_subsets = []
        for subset in prev_subsets:
            new_subsets.append(subset)
            new_subsets.append(subset + [num])
        return new_subsets


# Alvin's solutoin:
def subsets(elements):
  if not elements:
    return [[]]

  first = elements[0]
  remaining_elements = elements[1:]
  subsets_without_first = subsets(remaining_elements)

  subsets_with_first = []
  for sub in subsets_without_first:
    subsets_with_first.append([ first, *sub ])

  return subsets_without_first + subsets_with_first
