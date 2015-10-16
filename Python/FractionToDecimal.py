class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return 'NaN'
        result = ''
        # negative
        if numerator*denominator < 0:
            result += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        # integer part
        if numerator/denominator > 0:
            result += str(numerator/denominator)
        else:
            result += '0'
        # fraction dot or not
        if numerator%denominator > 0:
            result += '.'
        else:
            return result
        # fraction part
        table = {}
        remainder = numerator%denominator
        while remainder != 0:
            if remainder in table:
                return result[:table[remainder]] + '(' + result[table[remainder]:] + ')'
            else:
                result += str(remainder*10/denominator)
                table[remainder] = len(result)-1
            remainder = remainder*10%denominator
        return result
