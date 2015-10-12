class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1
        while left <= right:
            mid = (left+right)/2
            i, j = mid/n, mid%n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
