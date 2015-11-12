"""
evaluate reversed polish
input:
11 2 3 4 + + + 2 /
output:
10
"""
s = raw_input().strip().split(' ')

def evalRPN(tokens):
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
            de = stack.pop()
            nu = stack.pop()
            neg = -1 if de*nu < 0 else 1
            de = abs(de)
            nu = abs(nu)
            val = nu/de*neg
            stack.append(val)
    return stack[-1]
print evalRPN(s)                        
