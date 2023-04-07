# Write a function tribonacci that takes in a number argument, n, and returns the n-th number of the Tribonacci sequence.

# The 0-th and 1-st numbers of the sequence are both 0.

# The 2-nd number of the sequence is 1.

# To generate further numbers of the sequence, calculate the sum of previous three numbers.

# Solve this recursively.

# Mine and Alvin's solution:
def tribonacci(n):
  memo = {}
  return _trib(n, memo)

def _trib(n, memo):
  if n == 0 or n == 1:
    return 0
  
  if n == 2:
    return 1
  
  if n in memo:
    return memo[n]
  
  memo[n] = _trib(n -1 , memo) + _trib(n - 2, memo) + _trib(n - 3, memo)
  
  return memo[n]
