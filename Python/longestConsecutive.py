class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        result = 0
        count = {}
        for i in nums:
            if i in count:
                continue
            left = count[i-1] if i-1 in count else 0
            right = count[i+1] if i+1 in count else 0
            combine = left+1+right
            count[i] = 0
            count[i-left] = combine
            count[i+right] = combine
            result = max(result, combine)
        return result
