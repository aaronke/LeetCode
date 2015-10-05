class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        prev_reach = 0 # previous jump can reach range
        reach = nums[0] # second jump reach range, longest among all the candidates in the first range
        step = 0
        for i in range(0,len(nums)):
            if i > prev_reach:
                step += 1
                prev_reach = reach
            reach = max(reach, nums[i]+i)
            if reach <= i:
                return -1
            if reach >= len(nums)-1:
                return step+1
