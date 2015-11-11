# the essense of checking i > start is that with the save recursion call, avoid dups
def subsetsWithDup(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if nums is None:
        return []
    self.result = [[]]
    self.helper(sorted(nums), [], 0)
    return self.result
    
def helper(self, nums, one, start):
    if start >= len(nums):
        return
    for i in range(start, len(nums)):
        # make sure the coming element is not duplicated with previously removed
        if i > start and nums[i] == nums[i-1]:
            continue
        one.append(nums[i])
        self.helper(nums, one, i+1)
        self.result.append(one[:])
        del one[-1]
