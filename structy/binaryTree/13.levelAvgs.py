# level averages
# Write a function, level_averages, that takes in the root of a binary tree that contains number values. The function should return a list containing the average value of each level.


# My recursive Solution:
from statistics import mean
from collections import deque

def level_averages(root):
  levels = _fill_levels(root)
  
  avgs = []
  
  for level in levels:
    avgs.append(mean(level))
  return avgs

def _fill_levels(root):
  if root is None:
    return []
  levels = []
  queue = deque([(root, 0)])
  while queue:
    current, level = queue.popleft()
    if len(levels) == level:
      levels.append([current.val])
    else:
      levels[level].append(current.val)
    
    if current.left:
      queue.append((current.left, level +1))
      
    if current.right:
      queue.append((current.right, level +1))
  
  return levels


#Alvin's recursive solution:
from statistics import mean

def level_averages(root):
  levels = []
  fill_levels(root, levels, 0)
  
  avgs = []
  for level in levels:
    avgs.append(mean(level))
  return avgs
    
def fill_levels(root, levels, level_num):
  if root is None:
    return
  
  if level_num == len(levels):
    levels.append([ root.val ])
  else:
    levels[level_num].append(root.val)
  
  fill_levels(root.left, levels, level_num + 1)
  fill_levels(root.right, levels, level_num + 1)
