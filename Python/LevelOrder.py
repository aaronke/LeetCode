class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        if root == None:
            return []
        result = []
        queue = deque()
        queue.append(root)
        while len(queue) != 0:
            size = len(queue)
            this_level = []
            for i in range(size):
                node = queue.popleft()
                this_level.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            result.append(this_level)
        return result

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        queue = deque()
        result = []
        if root == None:
            return result
        queue.append(root)
        while len(queue) != 0:
            this_level = []
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                this_level.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            result.append(this_level)
        return result[::-1]        
