class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.search(board, 0)

    def search(self, board, n):
        if n == 81:
            return True
        i, j = n/9, n%9
        if board[i][j] != '.':
            return self.search(board, n+1)
        for num in range(1,10):
            board[i][j] = str(num)
            if self.isValidSudoku(board, i, j) and self.search(board,n+1):
                return True
            board[i][j] = '.'
        return False

    def isValidSudoku(self, board, ii, jj):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check rows
        flag = set()
        for j in range(9):
            if board[ii][j] == '.':
                continue
            if board[ii][j] in flag:
                return False
            flag.add(board[ii][j])
        
        # check cols
        flag = set()
        for i in range(9):
            if board[i][jj] == '.':
                continue
            if board[i][jj] in flag:
                return False
            flag.add(board[i][jj])
                
        # check boxes
        i, j = ii/3*3, jj/3*3
        flag = set()
        for m in range(3):
            for n in range(3):
                if board[i+m][j+n] == '.':
                    continue
                if board[i+m][j+n] in flag:
                    return False
                flag.add(board[i+m][j+n])
        return True        
