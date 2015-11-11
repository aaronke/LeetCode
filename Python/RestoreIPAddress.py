class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s is None or len(s) < 4 or len(s) > 12:
            return []
        result = []
        for i in xrange(1, len(s)-2):
            if not self.isValid(s[:i]):
                continue
            for j in xrange(i+1, len(s)-1):
                if not self.isValid(s[i:j]):
                    continue                
                for k in xrange(j+1, len(s)):
                    if not self.isValid(s[j:k]) or not self.isValid(s[k:]):
                        continue
                    result.append(s[:i]+'.'+s[i:j]+'.'+s[j:k]+'.'+s[k:])
        return result

    def isValid(self, s):
        if s[0] == '0' and len(s) > 1:
            return False
        return int(s) >= 0 and int(s) <= 255
