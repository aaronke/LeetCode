class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        slow, fast = 0, 2
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow+1] = nums[fast]
            fast += 1
        return slow+2
