class Solution(object):
    # move pos num to right position
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            # avoid duplicates swap for dead loop
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]: 
                self.swap(nums, i, nums[i]-1)
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums)+1
        
    def swap(self, nums, i, j):
        nums[i] ^= nums[j]
        nums[j] ^= nums[i]
        nums[i] ^= nums[j]
