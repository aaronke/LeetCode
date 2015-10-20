class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''
        if n == 1:
            return '1'
        prev = self.countAndSay(n-1)
        current = ''
        slow, fast = 0, 1
        length = 1
        while fast < len(prev):
            if prev[slow] == prev[fast]:
                length += 1
            else:
                current += str(length)+prev[slow]
                length = 1
                slow = fast
            fast += 1
        current += str(length)+prev[slow]
        return current
