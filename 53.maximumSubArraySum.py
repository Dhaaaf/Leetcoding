


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # brute force solution

        # length_n = len(nums)

        # if length_n == 1:
        #     return nums[0]

        # max_sum = nums[0]
        
        # for i in range(length_n -1):
        #     current_sum = nums[i]
        
        #     for j in range(i + 1, length_n):
        #         current_sum += nums[j]
        #         max_sum = max(max_sum, current_sum, nums[j])

        # return max_sum


        # Dynamic Programming Question

        length_n = len(nums)

        if length_n == 1:
            return nums[0]

        # Initialize our sums array
        # Add first value into array
        # Set max_sum
        # Keeps track of largest sum for the specific index
        sums = []
        sums.append(nums[0])
        max_sum = nums[0]

        # Iterate through the array
        # To our sums array we're going to append The max of sum, or the number itself
        for i in range(1, length_n):
            sums.append(max(sums[i-1] + nums[i], nums[i]))
            max_sum = max(max_sum, sums[i])

        # sums array

        return max_sum