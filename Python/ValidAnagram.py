class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        alphabet_table = {}
        if len(s) != len(t):
            return False
        # scan s
        for c in s:
            if c in alphabet_table:
                alphabet_table[c] += 1
            else:
                alphabet_table[c] = 1
        # match t
        for c in t:
            if c in alphabet_table:
                alphabet_table[c] -= 1
                if alphabet_table[c] == 0:
                    del alphabet_table[c]
            else:
                return False
        return True
