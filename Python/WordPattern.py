class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        match_table = {}
        dup_check = set()
        str = str.strip().split(' ')
        if len(pattern) != len(str):
            return False
        for p, word in zip(pattern, str):
            if p not in match_table:
                if word in dup_check:
                    return False
                dup_check.add(word)
                match_table[p] = word
            elif match_table[p] != word:
                return False
        return True
