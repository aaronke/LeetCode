    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) < 1:
            return 0
        stack = []
        sign = '+'
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
            elif s[i] in ['+','-','*','/']:
                sign = s[i]
                i += 1
            else:
                num = s[i]
                while i+1 < len(s) and s[i+1].isdigit():
                    i += 1
                    num += s[i]
                num = int(num)
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(num*stack.pop())
                elif sign == '/':
                    if stack[-1] < 0:
                        stack.append(-(-stack.pop()/num))
                    else:
                        stack.append(stack.pop()/num)
                i += 1
        return sum(stack)
