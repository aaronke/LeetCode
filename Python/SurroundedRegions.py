class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) < 1 or len(board[0]) < 1:
            return
        # mark boundry 'O' to '#'
        for i in range(len(board)):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            if board[i][-1] == 'O':
                self.dfs(board, i, len(board[0])-1)
        for j in range(1,len(board[0])-1):
            if board[0][j] == 'O':
                self.dfs(board, 0, j)
            if board[-1][j] == 'O':
                self.dfs(board, len(board)-1, j)
        # set inside 'O' to 'X', boundry '#' back to 'O'
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
    # recursive, stackoverflow in large cases, use stack to dfs iteratively, or queue bfs
    def dfs(self, board, i , j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'O':
            return
        board[i][j] = '#'
        self.dfs(board, i+1, j)
        self.dfs(board, i-1, j)
        self.dfs(board, i, j+1)
        self.dfs(board, i, j-1)
