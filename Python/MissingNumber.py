class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort, time O(N*lgN), space O(1)
        # bucket count, time O(N), space O(N)
        if nums is None or len(nums) < 1:
            return 0
        bucket = [True]*(len(nums)+1)
        for i in nums:
            bucket[i] = False
        return bucket.index(True)
        
        # mathematic
        missing = (0+n)*(n+1)/2
        return missing - sum(nums)
        
        missing = 0
        # bit manipulation
        for i in range(1, len(nums)+1):
            missing ^= i
            missing ^= nums[i-1]
        return missing        
