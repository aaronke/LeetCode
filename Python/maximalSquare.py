class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # top, left, top-left
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return 0
        m, n = len(matrix), len(matrix[0])
        table = [[0 for j in range(n+1)] for i in range(m+1)]
        result = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    table[i+1][j+1] = min(table[i][j+1], min(table[i+1][j], table[i][j])) + 1
                    result = max(result, table[i+1][j+1])
        return result*result
