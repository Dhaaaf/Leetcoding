# Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

# The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

# Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

# Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.


# Proper Solution:
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:        
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            
            if(l,r) in dp:
                return dp[(l, r)]
            
            even = True if (r-1) % 2 else False

            left = piles[l] if even else 0 
            right = piles[r] if even else 0 
            
            dp[(l, r)] = max( dfs(l+1, r) + left, dfs(l, r-1) + right )

            return dp[(l, r)]
        
        return dfs(0, len(piles - 1)) > (sum(piles) // 2)

    












# Imperfect solution
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:        
        return True