class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for i in range(n)]

    def createEdge(self, x, y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)

    def dfs(self, src, visited, res):
        res.append(src)
        visited[src] = True
        for node in self.adj[src]:
            if visited[node] == False:
                self.dfs(node, visited, res)

    def DFS_main(self, src):
        visited = [False] * self.n
        res = []
        self.dfs(src, visited, res)
        return res

n = int(input("Enter the number of nodes you want: "))
g = Graph(n)
m = int(input("Enter the number of edges you want: "))

for i in range(m):
    x, y = map(int, list(input().split()))
    g.createEdge(x, y)

result = g.DFS_main(0)
print(result)