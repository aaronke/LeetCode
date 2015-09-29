class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})
        
    def helper(self, s, wordDict, result_map):
        if s in result_map:
            return result_map[s]
        result = []
        for i in range(1,len(s)+1):
            if s[:i] in wordDict:
                if i == len(s):
                    result.append(s)
                    result_map[s] = result
                    return result
                other_result = self.helper(s[i:], wordDict, result_map)
                for r in other_result:
                    result.append(s[:i] + ' ' + r)
        result_map[s] = result
        return result
                    
