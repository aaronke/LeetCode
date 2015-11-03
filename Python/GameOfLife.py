class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 0->-1: has 3 neighbors
        # 1->-2: has 0,1,45678(except2,3)
        if board is None or len(board) < 1 or len(board[0]) < 1:
            return
        # temp update
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = self.count_neighbors(board, i, j)
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = -1
                else:
                    if count not in [2,3]:
                        board[i][j] = -2
        # set temp to 0,1        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] == -2:
                    board[i][j] = 0
        return

    def count_neighbors(self, board, i, j):
        # live neighbor means:1, or -2
        count = 0
        if i-1 >= 0 and j-1 >= 0 and board[i-1][j-1] in [1, -2]:    count += 1
        if i-1 >= 0 and board[i-1][j] in [1, -2]:   count += 1
        if i-1 >= 0 and j+1 < len(board[0]) and board[i-1][j+1] in [1, -2]: count += 1
        if j-1 >= 0 and board[i][j-1] in [1, -2]:   count += 1
        if j+1 < len(board[0]) and board[i][j+1] in [1, -2]:    count += 1
        if i+1 < len(board) and j-1 >= 0 and board[i+1][j-1] in [1, -2]:    count += 1
        if i+1 < len(board) and board[i+1][j] in [1, -2]:   count += 1   
        if i+1 < len(board) and j+1 < len(board[0]) and board[i+1][j+1] in [1, -2]: count += 1
        return count
