class Solution(object):
    # DFS directed graph, checking cycles
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in xrange(numCourses)]
        visited = [0 for _ in xrange(numCourses)] # 0: not visited; 1: safe visited; -1: unsafe visited
        # initial the graph
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])
        # DFS the graph
        for oneCourse in xrange(numCourses):
            if visited[oneCourse] == 0 and not self.dfs(oneCourse, graph, visited):
                return False
        return True
    
    def dfs(self, oneCourse, graph, visited):
        visited[oneCourse] = -1 # search begin, half visited
        for otherCourse in graph[oneCourse]:
            if visited[otherCourse] == -1 or visited[otherCourse] == 0 and not self.dfs(otherCourse, graph, visited):
                return False
        visited[oneCourse] = 1 # search done, safe visited
        return True
