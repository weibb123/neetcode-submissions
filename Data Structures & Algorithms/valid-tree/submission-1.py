class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # property of tree
        if len(edges) != n - 1:
            return False
        
        # build the graph
        graph = {i: [] for i in range(n)}

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u) # since it is undirected
        
        # use DFS to check cycle
        visited = [False] * n

        def dfs(node: int, prev: int) -> bool:
            if visited[node]:
                return False
            visited[node] = True
            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        
        # perform DFS starting from node 0
        if not dfs(0, -1):
            return False
        
        # ensure all nodes are visited
        return all(visited)

            
        

        