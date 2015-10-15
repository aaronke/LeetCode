class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set(nums)
        return len(s) != len(nums)
        
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k < 1 or len(nums) < 2:
            return False
        s = set([])
        # initialize set
        for i in range(k+1):
            if i == len(nums):
                return False
            if nums[i] in s:
                return True
            s.add(nums[i])
        for i in range(k+1,len(nums)):
            s.remove(nums[i-k-1])
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False        
