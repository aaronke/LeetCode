class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # + - ( ) a stack, num a stack, skip ' '
        stack_s = []
        stack_n = []
        symbol = set(['+', '-', '('])
        i = 0
        while i < len(s):
            c = s[i]
            i += 1
            if c == ' ':
                continue
            if c.isdigit():
                while i < len(s) and s[i].isdigit():
                    c += s[i]
                    i += 1
                if len(stack_s) == 0 or stack_s[-1] == '(':
                    stack_n.append(int(c))
                else:
                    case = stack_s.pop()
                    if case == '+':
                        stack_n.append(stack_n.pop()+int(c))
                    else:
                        stack_n.append(stack_n.pop()-int(c))
            elif c in symbol:
                stack_s.append(c)
            elif c == ')':
                stack_s.pop()
                if len(stack_s) != 0 and stack_s[-1] != '(':
                    case = stack_s.pop()
                    if case == '+':
                        stack_n.append(stack_n.pop()+stack_n.pop())
                    else:
                        stack_n.append(-stack_n.pop()+stack_n.pop())                
        return stack_n[0]
