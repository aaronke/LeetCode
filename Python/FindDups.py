class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) < 2:
            return None
        n = len(nums) - 1
        left, right = 1, n
        # left <= right is not appropriate, since left == right granteered to be the answer.
        while left < right:
            mid = (left+right)/2
            count = self.countGreater(nums, mid)
            if count > n-mid:
                left = mid + 1
            else:
                right = mid
        return right
        
    def countGreater(self, nums, val):
            count = 0
            for i in nums:
                if i > val:
                    count += 1
            return count
