class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # redundant connection -> when found a node have same parent
        rank = [1] * (len(edges) + 1)
        parent = [i for i in range(len(edges) + 1)]

        def find(n):
            # find parent
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(x, y):
            x, y = find(x), find(y)

            if x == y:
                return False
            if rank[x] > rank[y]:
                parent[y] = x # parent of y is x, since x is higher rank
                rank[x] += rank[y]
            
            else:
                parent[x] = y
                rank[y] += rank[x]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2): # if false, we found cycle
                return [n1, n2]

            
