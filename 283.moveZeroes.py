# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # iterative through the list
        # pointer that starts at 0 index - last non-zero index.
        # Another pointer to the current element in iteration

        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums [i], nums[j] = nums[j], nums[i]
                i += 1
