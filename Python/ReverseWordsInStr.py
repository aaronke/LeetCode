class Solution(object):
    # pointer style
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) < 1:
            return s
        left, right = 0, len(s)-1
        while left < len(s) and s[left] == ' ':
            left += 1
        while right >= 0 and s[right] == ' ':
            right -= 1
        result = ''
        while right >= left:
            cursor = right
            while cursor >= left and s[cursor] != ' ':
                cursor -= 1
            result += s[cursor+1:right+1] + ' '
            while cursor >= left and s[cursor] == ' ':
                cursor -= 1
            right = cursor
        return result[:-1]

    # Python list style    
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) < 1:
            return s
        s = s.strip().split(' ')
        result = ''
        for i in s[::-1]:
            if i != '':
                result += i + ' '
        return result[:-1]        
