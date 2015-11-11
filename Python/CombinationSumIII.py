# fix size, and element range(1,10), start = i+1, since only want increasing list
def combinationSum3(self, k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    if k < 1 or k > 9 or n < 1 or n > 45:
        return []
    self.result = []
    self.helper(k, n, [], 1)
    return self.result
    
def helper(self, k, n, one, start):
    if len(one) == k and n == 0:
        self.result.append(one[:])
        return
    if len(one) == k or n <= 0:
        return
    for i in range(start,10):
        if i in one:
            continue
        one.append(i)
        self.helper(k, n-i, one, i+1)
        del one[-1]
