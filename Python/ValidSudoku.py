class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check rows
        for i in range(9):
            flag = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in flag:
                    return False
                flag.add(board[i][j])
        
        # check cols
        for j in range(9):
            flag = set()
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in flag:
                    return False
                flag.add(board[i][j])
                
        # check boxes
        for i in [0,3,6]:
            for j in [0,3,6]:
                flag = set()
                for m in range(3):
                    for n in range(3):
                        if board[i+m][j+n] == '.':
                            continue
                        if board[i+m][j+n] in flag:
                            return False
                        flag.add(board[i+m][j+n])
        return True
