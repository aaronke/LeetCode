class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0]*n
        result[0] = nums[0]
        for i in range(1,n):
            result[i] = result[i-1]*nums[i]
        right = nums[-1]
        result[-1] = result[-2]
        for i in range(n-2,0,-1):
            result[i] = result[i-1]*right
            right *= nums[i]
        result[0] = right
        return result
