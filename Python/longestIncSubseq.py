class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # L[i] = 1 + max(L[:i] if nums[i] > it)
        if nums is None or len(nums) < 1:
            return 0
        dp_array_max = [1]*len(nums)
        for i in range(1, len(nums)):
            current_max = 1
            for j in range(i):
                if nums[i] > nums[j] and dp_array_max[j] >= current_max:
                    current_max = dp_array_max[j] + 1
            dp_array_max[i] = current_max
        return max(dp_array_max)
        
# similar with LCS, which is dp[i][j] = dp[i-1][j-1] + 1 if S[i]==T[j] else max(dp[i-1][j], dp[i][j-1])
