class Graph:
    # adjacency matrix
    ''' If the nodes in the graph are 1 based'''
    def __init__(self, n, m, edges, type="adjacencyList") -> None:
        self.n = n
        self.m = m
        self.edges = edges

        if type == "adjacencyList":
            self.list = [[0] for _ in range(n+1)]
            for u, v in edges:
                self.list[u].append(v)
                self.list[v].append(u)
        else:
            self.matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
            for u, v in edges:
                self.matrix[u][v] = 1
                self.matrix[v][u] = 1 # use this line for a undirected graph. Else comment it for a directed graph
        

    def displayGraph(self, type="adjacencyList"):
        
        if type == "adjacencyList":
            print(self.list)
        else:
            # print(self.matrix)
            n = len(self.matrix)
            for i in range(1, n):
                for j in range(1, n):
                    print(self.matrix[i][j], end=" ")
                print("\n")

    def BFS(self, root):
        '''
        SC - O(N)
        TC - Did not understand this
        '''
        res = []
        queue = [root]
        isVisited = [0 for _ in range(self.n+1)] # O(N)
        isVisited[root] = 1

        while queue:
            top = queue.pop(0)
            res.append(top)
            # getting the neighboring elements of the current node
            for i in self.list[top]:
                if i != 0 and isVisited[i] == 0:
                    isVisited[i] = 1
                    queue.append(i)
        return res
    
    def DFSGraph(self, root):
        '''
            SC - O(N)
            TC - 
        '''
        isVisited = [0 for _ in range(self.n+1)]
        res = []
        self.DFS(root, isVisited, res)
        return res
        

    def DFS(self, node, isVisited, res):
        isVisited[node] = 1
        res.append(node)
        for i in self.list[node]:
            if i != 0 and isVisited[i] == 0:
                self.DFS(i, isVisited, res)






n = 9
m = 9 
edges = [[1,2],[1,6],[2,3],[2,4],[6,7],[6,9],[4,5],[7,8] ,[5,8]]
#graph = Graph(n,m,edges)
#graph.displayGraph()
#print(graph.DFSGraph(1))

# print([[0 for _ in range(5)] for _ in range(5)])

def BFS(root, adjList):
    res = []
    queue = [root]
    visited = [0 for _ in range(len(adjList))]

    visited[root] = 1

    while queue:
        top = queue.pop(0)
        res.append(top)
        for i in adjList[top]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

    return res


def DFS(root, adjList):
    res = []
    stack = [root]
    visited = [0 for _ in range(len(adjList))]

    while stack:
        node = stack.pop()
        visited[node] = 1
        res.append(node)

        for i in adjList[node]:
            if visited[i] == 0:
                stack.append(i) 

def DFS_recursion(root, adjList):
    visited = [0 for _ in range(len(adjList))]
    res = []
    dfs(root, visited, res, adjList)

def dfs(root, visited, res, adjList):
    visited[root] = 1
    res.append(root)

    for i in adjList[root]:
        if visited[i] == 0:
            dfs(i)
            



adjList = [[1,2],[0, 4,3], [0,3],[1,2],[1]]

print(BFS(0, adjList))


