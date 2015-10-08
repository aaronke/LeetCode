class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 1:
            return [-1,-1]
        start, end = -1, -1
        start = self.bs(nums, target-0.1)+1
        end = self.bs(nums, target+0.1)
        return [start, end] if start<=end else [-1,-1]
        
    def bs(self, nums, target):
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)/2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right
