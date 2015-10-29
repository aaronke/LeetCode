class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        result, cur_min, cur_max = nums[0], nums[0], nums[0]
        for i in nums[1:]:
            if i < 0:
                cur_min, cur_max = cur_max, cur_min
            cur_min = min(cur_min*i, i)
            cur_max = max(cur_max*i, i)
            result = max(result, cur_max)
        return result
