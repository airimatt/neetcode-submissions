class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        if not edges: return n
        
        # what means new component:
        # when we are going from one node to the next, there is no path to get to that node
        # so first create adj list
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        numComponents = 0
        visited = set()

        def dfs(node):
            if node in visited:
                return 0
            if not adj[node]:
                return 1
            
            visited.add(node)
            for c in adj[node]:
                dfs(c)
            
            adj[node] = []
            return 1

        # then go thru it with dfs
        # have a visited list so we don't double count components

        for i in range(n):
            numComponents += dfs(i)

        return numComponents

        