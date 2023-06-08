# Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

# The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

# Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

# Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.




# Imperfect solution
from collections import deque
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:        
        piles = deque(piles)
        alice_counter= 0
        bob_counter = 0
        turn_counter= 0 
        while piles:
            if piles[0] > piles[-1]:
                biggest_pile = piles[0]
                biggest_index = 0
            else:
                biggest_pile = piles[-1]
                biggest_index = -1
            if turn_counter % 2 == 0:
                alice_counter += biggest_pile
                if biggest_index == 0:
                    piles.popleft()
                else:
                    piles.pop()
            else:
                bob_counter += biggest_pile
                if biggest_index == 0:
                    piles.popleft()
                else:
                    piles.pop()    
        turn_counter +=1    
        return alice_counter > bob_counter 