class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) < 1:
            return []
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            tmp = digits[i] + carry
            if tmp == 10:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = tmp
                return digits
        digits.insert(0,1)
        return digits
