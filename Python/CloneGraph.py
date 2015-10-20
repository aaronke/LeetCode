# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node == None:
            return None
        from collections import deque
        bfs_queue = deque() # queue, to bfs the original graph
        result_map = {} # hashmap, to store the cloned nodes
        first_node = UndirectedGraphNode(node.label)
        bfs_queue.append(node)
        result_map[node.label] = first_node
        # begin bfs clone
        while len(bfs_queue) > 0:
            this_node = bfs_queue.popleft()
            clone_node = result_map[this_node.label]
            for neighbor in this_node.neighbors:
                if neighbor.label in result_map:
                    clone_neighbor = result_map[neighbor.label]
                    clone_node.neighbors.append(clone_neighbor)
                else:
                    clone_neighbor = UndirectedGraphNode(neighbor.label)
                    clone_node.neighbors.append(clone_neighbor)
                    result_map[neighbor.label] = clone_neighbor
                    bfs_queue.append(neighbor)
        return first_node
