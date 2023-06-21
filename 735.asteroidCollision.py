# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            # Only need to resolve conflicts when
            # Stack is not empty
            # current asteroid is negative
            # top of the stack is positive.
            while len(stack) and asteroid < 0 and stack[-1] > 0:    
                if stack[-1] == -asteroid:
                    stack.pop()
                    break
                elif stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] > -asteroid:
                    break
            else: 
                stack.append(asteroid)
        return stack
                