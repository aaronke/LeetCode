class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) < 1 or len(matrix[0]) < 1 or target is None:
            return False
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n-1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False
