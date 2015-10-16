class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) < 1:
            return 0
        stack = []
        for c in tokens:
            if len(c) > 1 or c.isdigit():
                stack.append(int(c))
            elif c == '+':
                stack.append(stack.pop()+stack.pop())
            elif c == '-':
                stack.append(-stack.pop()+stack.pop())
            elif c == '*':
                stack.append(stack.pop()*stack.pop())
            elif c == '/':
                # python / for negative values is weird
                de = stack.pop()
                nu = stack.pop()
                neg = -1 if de*nu < 0 else 1
                de = abs(de)
                nu = abs(nu)
                val = nu/de*neg
                stack.append(val)
        return stack[-1]
