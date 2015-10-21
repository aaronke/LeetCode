class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWord = False
        self.children = [None]*26

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        runner = self.root
        for c in word:
            if runner.children[ord(c)-ord('a')] == None:
                runner.children[ord(c)-ord('a')] = TrieNode()
            runner = runner.children[ord(c)-ord('a')]
        runner.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        runner = self.root
        for c in word:
            if runner.children[ord(c)-ord('a')] == None:
                return False
            runner = runner.children[ord(c)-ord('a')]
        return runner.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        runner = self.root
        for c in prefix:
            if runner.children[ord(c)-ord('a')] == None:
                return False
            runner = runner.children[ord(c)-ord('a')]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
