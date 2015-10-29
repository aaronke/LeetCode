class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import sys
        if grid == None or len(grid) < 1 or len(grid[0]) < 1:
            return 0
        dp = [sys.maxint]*(len(grid[0])+1)
        dp[1] = 0
        for i in range(len(grid)):
            for j in range(1,len(grid[0])+1):
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j-1]
        return dp[-1]
