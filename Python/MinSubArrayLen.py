class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) < 1:
            return 0
        slow, fast = 0, 0
        min_size = len(nums)+1
        current_sum = 0
        # initial fast pointer to the first one which satisfy the sum subarray
        while fast < len(nums) and current_sum + nums[fast] < s:
            current_sum += nums[fast]
            fast += 1
        while fast < len(nums):
            current_sum += nums[fast]
            # update slow pointer
            while slow < fast and current_sum - nums[slow] >= s:
                current_sum -= nums[slow]
                slow += 1
            min_size = min(min_size, fast-slow+1)
            fast += 1
        return min_size if min_size != len(nums)+1 else 0
