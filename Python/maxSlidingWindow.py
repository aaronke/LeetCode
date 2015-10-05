class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deque = collections.deque()
        result = []
        # init first k elements
        for i in range(k):
            while len(deque)>0 and nums[deque[-1]] <= nums[i]:
                deque.pop()
            deque.append(i)
        if len(deque) > 0:
            result.append(nums[deque[0]])
        # sliding
        for i in range(k,len(nums)):
            if deque[0] == i-k:
                deque.popleft()
            while len(deque)>0 and nums[deque[-1]] <= nums[i]:
                deque.pop()
            deque.append(i)
            result.append(nums[deque[0]])
        return result
