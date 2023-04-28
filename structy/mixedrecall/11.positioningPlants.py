# You've been hired to plant flowers in a garden with n different positions. There are m different flower types. The prices of flowers types vary depending on which position they are planted. Your bosses are picky, they tell you to never plant two of the same flower type right next to each other. What is the minimum cost we need to plant a flower in each position of the garden?

# Write a function, positioningPlants, that takes in a 2D list with dimensions n * m. Each row of the list represents the costs of the flower types at that position. This means that costs[i][j] represents the cost of planting flower type j at position i. For example:

def positioning_plants(costs):
  return _positioning_plants(costs, 0, None, {})

def _positioning_plants(costs, pos, last_plant, memo):
  key = (pos, last_plant)
  if key in memo:
    return memo[key]
  
  if pos == len(costs):
    return 0
  
  min_cost = float('inf')
  
  for plant, cost in enumerate(costs[pos]):
    if plant != last_plant:
      candidate = cost + _positioning_plants(costs, pos + 1, plant, memo)
      min_cost = min(candidate, min_cost)
  
  memo[key] = min_cost
  return min_cost
