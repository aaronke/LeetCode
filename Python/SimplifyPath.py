class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if len(path) < 1:
            return ''
        stack = []
        result = ''
        path = path.strip().split('/')
        print path
        for p in path:
            if p == '.' or p == '':
                continue
            if p == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        for p in stack:
            result += '/' + p
        if len(result) == 0:
            return '/'
        return result
