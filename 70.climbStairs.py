# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



class Solution:
    def climbStairs(self, n: int) -> int:

        a, b = 0, 1
        for i in range(n):
            a, b = b, b + a
            1, 1, 2, 3, 5, 8, 13, 21, 
        return b
