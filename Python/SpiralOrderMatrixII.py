class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        result = [[0 for i in range(n)] for i in range(n)]
        val = 1
        for cycle in range(n/2+n%2):
            # up
            for i in range(cycle, n-cycle):
                result[cycle][i] = val
                val += 1
            # right
            if n-cycle-1 == cycle:
                break            
            for i in range(cycle+1, n-cycle-1):
                result[i][n-cycle-1] = val
                val += 1
            # down
            for i in range(n-2*cycle):
                result[n-cycle-1][n-cycle-1-i] = val
                val += 1
            # left
            for i in range(1,n-2*cycle-1):
                result[n-cycle-1-i][cycle] = val
                val += 1
        return result
