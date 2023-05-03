# binary search
# Write a function, binary_search, that takes in a sorted list of numbers and a target. The function should return the index where the target can be found within the list. If the target is not found in the list, then return -1.

# You may assume that the input array contains unique numbers sorted in increasing order.

# Your function must implement the binary search algorithm.



def binary_search(numbers, target):
  left, right = 0, len(numbers) - 1
  
  while left <= right:
    mid = (left + right) // 2
    if target == numbers[mid]:
      return mid
    if target < numbers[mid]:
      right = mid - 1
    if target > numbers[mid]:
      left = mid + 1
  return -1
