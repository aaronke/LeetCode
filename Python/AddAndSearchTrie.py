class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie['#'] = '#'

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.__dfs__(word, self.trie)
        
    def __dfs__(self, word, trie):
        if len(word) == 0:
            return '#' in trie
        c = word[0]
        if c == '.':
            for cc in trie:
                if cc != '#' and self.__dfs__(word[1:], trie[cc]):
                    return True
            return False
        else:
            if c not in trie:
                return False
            else:
                trie = trie[c]
                return self.__dfs__(word[1:], trie)

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
