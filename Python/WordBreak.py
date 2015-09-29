class Solution(object):
    # Brute Force, TLE
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if len(s) < 1 and s not in wordDict:
            return False
        return self.helper(s, wordDict, 0)
        
    def helper(self, s, wordDict, i_start):
        if (i_start == len(s)):
            return True
        for i in range(i_start+1,len(s)+1):
            if s[i_start:i] in wordDict:
                if self.helper(s, wordDict, i):
                   return True
        return False
