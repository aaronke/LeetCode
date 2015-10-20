    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < 1 or k > n or k < 1:
            return []
        self.result = []
        self.helper(n, k, 1, [])
        return self.result
        
    def helper(self, n, k, start, one_combination):
        if len(one_combination) == k:
            self.result.append(one_combination[:])
            return
        for i in range(start, n+1):
            one_combination.append(i)
            self.helper(n, k, i+1, one_combination)
            del one_combination[-1]
