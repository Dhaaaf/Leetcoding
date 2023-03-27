
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.



class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Brute force version:
        # Set variable for a maximum water
        # Nested Loop through array O(n^2)

        # Two pointer solution
        # Theoretical max set variable here
        #find smalles pointer, increment it
        # recalculate the water
        # Keep going until left = right

        left = 0
        right = len(height)-1
        max_water = 0

        while left != right:
            new_water = min(height[left], height[right])*(right - left)
            if new_water > max_water:
                max_water = new_water
            if height[left] < height[right]:
                left += 1
            else:
                right -=1

        return max_water
