# Write a function, array_stepper, that takes in a list of numbers as an argument. You start at the first position of the list. The function should return a boolean indicating whether or not it is possible to reach the last position of the list. When situated at some position of the list, you may take a maximum number of steps based on the number at that position.

# My iterative greedy solution:
def array_stepper(numbers):
  n = len(numbers)
  if n <=1:
    return True
  
  last_point = n-1
  for i in range(n-1,-1,-1):
    if numbers[i] >= last_point -i:
      last_point = i
  
  return last_point == 0


# Alvin's dynamic recursive solution:
def array_stepper(numbers):
  return _array_stepper(numbers, 0, {})

def _array_stepper(numbers, i, memo):
  if i in memo:
    return memo[i]
  
  if i >= len(numbers) - 1:
    return True
  
  max_step = numbers[i]
  for step in range(1, max_step + 1):
    if _array_stepper(numbers, i + step, memo):
      memo[i] = True
      return True
    
  memo[i] = False  
  return False
