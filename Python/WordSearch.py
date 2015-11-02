class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board is None or word is None or len(board) < 1 or len(board[0]) < 1:
            return False
        isVisited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, 0, isVisited):
                    return True
        return False
        
    def dfs(self, board, i, j, word, cursor, isVisited):
        """
        dfs word from point (i,j)
        """
        if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1 or isVisited[i][j] or board[i][j] != word[cursor]:
            return False
        if cursor == len(word) - 1:
            return True
        isVisited[i][j] = True
        flag = self.dfs(board, i-1, j, word, cursor+1, isVisited) or self.dfs(board, i+1, j, word, cursor+1, isVisited) or self.dfs(board, i, j-1, word, cursor+1, isVisited) or self.dfs(board, i, j+1, word, cursor+1, isVisited)
        isVisited[i][j] = False
        return flag
