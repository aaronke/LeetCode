# use set() to speed up check in or not
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, s):
        runner = self.root
        for c in s:
            if c not in runner.children:
                runner.children[c] = TrieNode()
            runner = runner.children[c]
        runner.isWord = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if board is None or words is None or len(board) < 1 or len(board[0]) < 1:
            return []
        result = set()
        trie = Trie()
        for word in words:
            trie.insert(word)
        isVisited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie.root, result, isVisited, '')
        return list(result)

    def dfs(self, board, i, j, trie, result, isVisited, path):
        """
        dfs word from point (i,j)
        """
        if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1 or isVisited[i][j] or board[i][j] not in trie.children:
            return False
        path += board[i][j]
        isVisited[i][j] = True
        if trie.children[board[i][j]].isWord and path not in result:
            result.add(path)
        flag = self.dfs(board, i-1, j, trie.children[board[i][j]], result, isVisited, path) or self.dfs(board, i+1, j, trie.children[board[i][j]], result, isVisited, path) or self.dfs(board, i, j-1, trie.children[board[i][j]], result, isVisited, path) or self.dfs(board, i, j+1, trie.children[board[i][j]], result, isVisited, path)
        isVisited[i][j] = False
        path = path[:-1]
        return flag

# Trie complete version
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, s):
        runner = self.root
        for c in s:
            if c not in runner.children:
                runner.children[c] = TrieNode()
            runner = runner.children[c]
        runner.isWord = True
            
    def search(self, s):
        runner = self.root
        for c in s:
            if c not in runner.children:
                return False
            runner = runner.children[c]
        return runner.isWord
        
    def contains(self, s):
        runner = self.root
        for c in s:
            if c not in runner.children:
                return False
            runner = runner.children[c]
        return True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if board is None or words is None or len(board) < 1 or len(board[0]) < 1:
            return []
        result = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        isVisited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie, result, isVisited, '')
        return result

    def dfs(self, board, i, j, trie, result, isVisited, path):
        """
        dfs word from point (i,j)
        """
        if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1 or isVisited[i][j] or not trie.contains(path+board[i][j]):
            return False
        path += board[i][j]
        isVisited[i][j] = True
        if trie.search(path) and path not in result:
            result.append(path)
        flag = self.dfs(board, i-1, j, trie, result, isVisited, path) or self.dfs(board, i+1, j, trie, result, isVisited, path) or self.dfs(board, i, j-1, trie, result, isVisited, path) or self.dfs(board, i, j+1, trie, result, isVisited, path)
        isVisited[i][j] = False
        path = path[:-1]
        return flag
