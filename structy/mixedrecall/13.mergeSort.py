# Write a function, merge_sort, that takes in a list of numbers as an argument. The function should return a new list containing elements of the original list sorted in ascending order. Your function must implement the merge sort algorithm.





from collections import deque

def merge_sort(nums):
  if len(nums) <= 1:
    return nums
  mid_idx = len(nums)//2
  left_sorted = merge_sort(nums[:mid_idx])
  right_sorted = merge_sort(nums[mid_idx:])
  return merge(left_sorted, right_sorted)

def merge(list_1, list_2):
  list_1 = deque(list_1)
  list_2 = deque(list_2)
  
  merged = []
  while list_1 and list_2:
    if list_1[0] < list_2[0]:
      merged.append(list_1.popleft())
    else:
      merged.append(list_2.popleft())
  merged += list_1
  merged += list_2
  return merged
