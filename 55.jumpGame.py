# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Brute force solution
        # a lot of nested for loops

        # if when we start from beginning if we can hit the end specifically

        # if we start at the end and go backwards?

        n = len(nums)
        if n <= 1:
            return True
        
        last_point = n-1
        for i in range(n-1, -1, -1):
            if nums[i] >= last_point - i:
                last_point = i

        return last_point == 0
