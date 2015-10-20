class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ''
        carry = 0
        i, j = len(a)-1, len(b)-1
        while i >= 0 and j >= 0:
            state = int(a[i])+int(b[j])+carry
            if state == 0:
                result += '0'
            elif state == 1:
                result += '1'
                carry = 0
            elif state == 2:
                result += '0'
                carry = 1
            elif state == 3:
                result += '1'
                carry = 1
            i -= 1
            j -= 1
        while i >= 0:
            state = int(a[i])+carry
            if state == 0:
                result += '0'
            elif state == 1:
                result += '1'
                carry = 0
            elif state == 2:
                result += '0'
                carry = 1
            i -= 1
        while j >= 0:
            state = int(b[j])+carry
            if state == 0:
                result += '0'
            elif state == 1:
                result += '1'
                carry = 0
            elif state == 2:
                result += '0'
                carry = 1
            j -= 1
        if carry == 1:
            result += '1'
        return result[::-1]
