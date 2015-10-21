class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        result = nums[0]
        for i in nums[1:]:
            if i == result:
                count += 1
            elif count == 0:
                result = i
                count = 1
            else:
                count -= 1
        return result
