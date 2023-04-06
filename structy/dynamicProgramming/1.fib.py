# Write a function fib that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.

# The 0-th number of the sequence is 0.

# The 1-st number of the sequence is 1.

# To generate further numbers of the sequence, calculate the sum of previous two numbers.

# Solve this recursively.



# Memoization solution:
def fib(n):
  memo ={}
  return _fib(n, memo)

def _fib(n, memo):
  if n == 0:
    return 0
  if n == 1:
    return 1
  
  if n in memo:
    return memo[n]
  
  memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
  
  return memo[n]


#Brute force solution:
def fib(n):
  if n == 0 or n == 1:
    return n
  return fib(n - 1) + fib(n - 2)
