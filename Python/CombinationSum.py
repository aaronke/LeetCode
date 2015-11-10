# can reuse elements multiple times, start = i
def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if candidates is None or target is None or len(candidates) < 1:
        return []
    self.result = []
    self.helper(sorted(candidates), target, [], 0)
    return self.result
    
def helper(self, candidates, target, one, start):
    if target == 0:
        self.result.append(one[:])
        return
    if target < 0:
        return
    for i in range(start, len(candidates)):
        c = candidates[i]
        one.append(c)
        self.helper(candidates, target-c, one, i)
        del one[-1]
