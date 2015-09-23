class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        start = 0
        end = 0
        current_len = 0
        result = []
        while end < len(words):
            current_len += len(words[end]) + 1
            if current_len <= maxWidth + 1:
                end += 1
            else:
                result.append(self.oneline(words[start:end],maxWidth))
                start = end
                current_len = 0
        lastline = ''
        for i in range(start, end):
            lastline += words[i] + ' '
        lastline = lastline[:-1] + (maxWidth-len(lastline)+1)*' '
        result.append(lastline)
        return result

    def oneline(self,words, maxWidth):
        if len(words) == 1:
            return words[0] + (maxWidth-len(words[0]))*' '
        if len(words) == 2:
            return words[0] + (maxWidth-len(words[0]) - len(words[1]))*' ' + words[1]
        all_c = 0
        for s in words:
            all_c += len(s)
        all_space = maxWidth - all_c
        each_space = all_space/(len(words)-1)
        remain = all_space%(len(words)-1)
        result = ''
        for i in range(len(words)-1):
            if remain > 0:
                extra = 1
                remain -= 1
            else:
                extra = 0
            result += words[i]
            result += ' '*(each_space+extra)
        result += words[-1]
        return result
