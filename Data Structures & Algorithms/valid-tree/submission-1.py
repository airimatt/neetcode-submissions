class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not n:
            return True
        
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)


        visited = set()
        def dfs(node, prev):
            if node in visited:
                print("already visited node:", node)
                return False
            
            visited.add(node)
            for c in adj[node]:
                print("child:", c)
                if c == prev:
                    continue
                if not dfs(c, node):
                    return False

            return True
       
        return dfs(0, -1) and len(visited) == n