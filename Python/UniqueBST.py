class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[n] = left part * right part, range part size from 0 to n-1
        dp = [1,1]+[0]*(n-1)
        for i in range(2,n+1):
            for partition in range(i):
                dp[i] += dp[partition]*dp[i-partition-1]
        return dp[-1]
