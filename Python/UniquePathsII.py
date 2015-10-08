class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 1 or n < 1:
            return 0
        table = [[1 for i in range(n)] for i in range(m)]
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                table[i][j] = table[i+1][j] + table[i][j+1]
        return table[0][0]
        
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) < 1 or len(obstacleGrid[0]) < 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        table = [[1 for i in range(n)] for i in range(m)]
        # bot
        for i in range(m-2,-1,-1):
            table[i][n-1] = table[i+1][n-1] if obstacleGrid[i][n-1] == 0 else 0
        # right
        for i in range(n-2,-1,-1):
            table[m-1][i] = table[m-1][i+1] if obstacleGrid[m-1][i] == 0 else 0        
        # inside
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if obstacleGrid[i][j] == 1:
                    table[i][j] = 0
                else:
                    table[i][j] = table[i+1][j] + table[i][j+1]
        return table[0][0]        
