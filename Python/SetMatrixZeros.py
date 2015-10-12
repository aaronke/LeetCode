class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return
        m, n = len(matrix), len(matrix[0])
        flag_row, flag_col = -1, -1
        # find & set flag row and col
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if flag_row == -1:
                        flag_row, flag_col = i, j
                    else:
                        matrix[flag_row][j] = 0
                        matrix[i][flag_col] = 0
        if flag_row == -1:
            return
        # set flags in the row
        for j in range(n):
            if j == flag_col:
                continue
            if matrix[flag_row][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        # set flags in the col
        for i in range(m):
            if matrix[i][flag_col] == 0:
                for j in range(n):
                    matrix[i][j] = 0
            # set last col
            matrix[i][flag_col] = 0
        return
                        
