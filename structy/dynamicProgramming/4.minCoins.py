# Write a function min_change that takes in an amount and a list of coins. The function should return the minimum number of coins required to create the amount. You may use each coin as many times as necessary.

# If it is not possible to create the amount, then return -1.



def min_change(amount, coins):
  ans = _min_change(amount, coins, {})
  if ans == float('inf'):
    return -1
  else:
    return ans


def _min_change(amount, coins, memo):
  if amount in memo:
    return memo[amount]
  
  if amount == 0:
    return 0
  
  if amount < 0:
    return float('inf')
  
  min_coins = float('inf')
  for coin in coins:
    num_coins = 1 + _min_change(amount - coin, coins, memo)
    min_coins = min(min_coins, num_coins)
    
  memo[amount] = min_coins
  return min_coins
