class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) < 1:
            return []
        m, n = len(matrix), len(matrix[0])
        if n < 1:
            return []
        result = []
        for cycle in range(min(m,n)/2+min(m,n)%2):
            # up
            for i in range(cycle, n-cycle):
                result.append(matrix[cycle][i])
            # right
            if m-cycle-1 == cycle:
                break            
            for i in range(cycle+1, m-cycle-1):
                result.append(matrix[i][n-cycle-1])
            # down
            if n-cycle-1 == cycle:
                break            
            for i in range(n-2*cycle):
                result.append(matrix[m-cycle-1][n-cycle-1-i])
            # left
            for i in range(1,m-2*cycle-1):
                result.append(matrix[m-cycle-1-i][cycle])
        return result
