class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        result = nums[0]
        carry = nums[0]
        for i in nums[1:]:
            if carry < 0:
                carry = 0
            carry += i
            result = max(result, carry)
        return result
