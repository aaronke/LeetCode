class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n < 2:
            return
        for cycle in range(n/2):
            for i in range(cycle,n-cycle-1):
                temp = matrix[cycle][i]
                matrix[cycle][i], matrix[n-i-1][cycle], matrix[n-cycle-1][n-i-1], matrix[i][n-cycle-1] = matrix[n-i-1][cycle], matrix[n-cycle-1][n-i-1], matrix[i][n-cycle-1], temp
