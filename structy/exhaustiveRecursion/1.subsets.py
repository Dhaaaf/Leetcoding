# Write a function, subsets, that takes in a list as an argument. The function should return a 2D list where each sublist represents one of the possible subsets of the list.

# The elements within the subsets and the subsets themselves may be returned in any order.

# You may assume that the input list contains unique elements.


# Iterative

def subsets(nums):
    res = [[]]
    for num in nums:
        for subset in res[:]:
            res.append(subset + [num])
    return res



# My Recursive

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
