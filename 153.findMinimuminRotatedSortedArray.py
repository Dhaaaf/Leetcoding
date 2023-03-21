# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.


class Solution:
    def findMin(self, nums: List[int]) -> int:

        # if length of list = 1, then we can return nums[0]

        # loop through array and find minimum ===> O(n)

        # binary search, issue is we need a left and right pointer

        # midpoint 
        # if midpoint > mid+1.  mid +1 === min
        # if midpoint < mid - 1 mid === min

        # if right > mid right === mid -1
        # if right < mid left === mid +1

        length = len(nums)

        if length == 1:
            return nums[0]

        l, r = 0, length - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > nums[mid+1]:
                return nums[mid+1]

            if nums[mid] < nums[mid-1]:
                return nums[mid]

            if nums[r] > nums[mid]:
                r = mid -1
            else:
                l = mid + 1
