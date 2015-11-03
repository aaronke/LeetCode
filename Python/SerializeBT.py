# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        level_order = []
        queue = deque()
        if root is not None:
            queue.append(root)
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node is None:
                    level_order.append('None')
                else:
                    level_order.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
        return ','.join(level_order)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data is None or len(data) < 1:
            return None
        data = data.split(',')
        root = TreeNode(int(data[0]))
        queue = deque()
        queue.append(root)
        i = 1
        while i < len(data):
            runner = queue.popleft()
            if data[i] != 'None':
                runner.left = TreeNode(int(data[i]))
                queue.append(runner.left)
            i += 1
            if data[i] != 'None':
                runner.right = TreeNode(int(data[i]))
                queue.append(runner.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
