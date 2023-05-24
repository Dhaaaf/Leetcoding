
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.







class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for index in range(len(nums)):
            if nums[index] > 0:
                break
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            left, right = index + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < 0 - nums[index]:
                    left += 1
                elif nums[left] + nums[right] > 0 - nums[index]:
                    right -= 1
                else:
                    result.append([nums[index], nums[left], nums[right]]) # After a triplet is appended, we try our best to incease the numeric value of its first element or that of its second.
                    left += 1 # The other pairs and the one we were just looking at are either duplicates or smaller than the target.
                    right -= 1 # The other pairs are either duplicates or greater than the target.
                    # We must move on if there is less than or equal to one integer in between the two nums.
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1 # The pairs are either duplicates or smaller than the target.
        return result