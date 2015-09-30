class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        previous_max = 0
        current_max = 0
        all_max = 0
        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                if len(stack) == 0:
                    previous_max = 0
                else:
                    current_max = i - stack.pop() + 1
                    if len(stack) == 0:
                        current_max += previous_max
                        previous_max = current_max
                        all_max = max(all_max, current_max)
                        current_max = 0
                    else:
                        current_max = i - stack[-1]
                        all_max = max(all_max, current_max)
            elif s[i] == '(':
                stack.append(i)
        return all_max
