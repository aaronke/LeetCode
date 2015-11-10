# can only use elements once, start = i+1
# remove dups: avoid starting from the same element
def combinationSum2(self, candidates, target):
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
    if target == 0 and one not in self.result:
        self.result.append(one[:])
        return
    if target < 0:
        return
    for i in range(start, len(candidates)):
        # make sure the first element is not duplicated
        if len(one) == 0 and i-1 >= 0 and candidates[i] == candidates[i-1]:
            continue
        one.append(candidates[i])
        self.helper(candidates, target-candidates[i], one, i+1)
        del one[-1]
