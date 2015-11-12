"""
Given directed edges. Check it represents a tree or not.
input:
a b
a c
c d
b d
output:
false
"""
vertexs = set([])
edges = []
flag = True
while flag:
    try:
        a = raw_input()
        a = a.strip().split(' ')
        vertexs.add(a[0])
        vertexs.add(a[1])
        edges.append([a[1],a[0]])
    except:
        flag = False
        break
graph = {}
graph_reverse = {}
visited = {}
for edge in edges:
    graph[edge[0]] = []
    graph_reverse[edge[1]] = []    
for edge in edges:    
    graph[edge[0]].append(edge[1])
    graph_reverse[edge[1]].append(edge[0])
for v in vertexs:
    visited[v] = 0
    if v not in graph:
        graph[v] = []
    if v not in graph_reverse:
        graph_reverse[v] = []
#print graph
#print visited
class Solver(object):
    def findOrder(self, graph, visited):
        self.result = []
        # DFS the graph
        for k in visited.keys():
            if visited[k] == 0 and not self.dfs(k, graph, visited):
                self.result = []
                return
    
    def dfs(self, k, graph, visited):
        visited[k] = -1 # search begin, half visited
        for kk in graph[k]:
            if visited[kk] == -1 or visited[kk] == 0 and not self.dfs(kk, graph, visited):
                return False
        visited[k] = 1 # search done, safe visited
        self.result.append(k)
        return True
    
    def verifySingleTree(self, graph, visited, graph_reverse):
        self.findOrder(graph, visited)
        #print self.result
        if self.result == []:
            return False
        self.result_reverse = []
        self.dfs_reverse(self.result[0], graph_reverse)
        #print self.result_reverse
        return len(self.result_reverse) == len(self.result)
        
    def dfs_reverse(self, k, graph):
        self.result_reverse.append(k)
        if k not in graph:
            return
        for kk in graph[k]:
            self.dfs_reverse(kk, graph)
            
solver = Solver()
if solver.verifySingleTree(graph, visited, graph_reverse):
    print "true"
else:
    print "false"
