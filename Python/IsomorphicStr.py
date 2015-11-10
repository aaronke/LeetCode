    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None or len(s) != len(t):
            return False
        compareMap = {}
        replaceSet = set([])
        for i in xrange(len(s)):
            if s[i] in compareMap and compareMap[s[i]] != t[i]:
                return False
            if s[i] not in compareMap and t[i] in replaceSet:
                return False
            compareMap[s[i]] = t[i]
            replaceSet.add(t[i])
        return True
