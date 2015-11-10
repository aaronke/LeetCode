    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        self.digit_mapping = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine',
        'Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen',
        'Nineteen','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        self.unit_mapping = ['Thousand','Million','Billion']
        unit_count = 0
        result = self.threeDigitsToWords(num%1000)
        while num/1000 > 0:
            num /= 1000
            threeDigits = self.threeDigitsToWords(num%1000)
            if threeDigits != '':
                result = threeDigits + ' ' + self.unit_mapping[unit_count] + ' ' + result
            unit_count += 1
        return result.strip()

    def threeDigitsToWords(self, num):
        if num == 0:
            return ''
        result = ''
        if num%100 <= 20:
            result = self.digit_mapping[num%100]
        else:
            result = self.digit_mapping[num%100/10+18] + ' ' + self.digit_mapping[num%100%10]
        if num/100 > 0:
            result = self.digit_mapping[num/100] + ' Hundred ' + result
        return result.strip()
