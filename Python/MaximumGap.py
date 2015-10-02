class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N < 2:
            return 0
        max_bound, min_bound = max(nums), min(nums)
        bucket_gap = (max_bound - min_bound)/(N - 1) + 1
        min_bucket = [max_bound]*(N - 1)
        max_bucket = [min_bound]*(N - 1)
        for i in nums:
            if i == max_bound or i == min_bound:
                continue
            idx = (i - min_bound)/bucket_gap
            min_bucket[idx] = min(i, min_bucket[idx])
            max_bucket[idx] = max(i, max_bucket[idx])
        previous = min_bound
        max_gap = 0
        for i in range(N-1):
            if min_bucket[i] == max_bound:
                continue
            max_gap = max(max_gap, min_bucket[i] - previous)
            previous = max_bucket[i]
        return max(max_gap, max_bound - previous)
