class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, node):
        # this function finds the root of the set 
        # continuously points each node's parent to its grandparent until reaches root
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur
    
    def union(self, u, v):
        # finds the root containing u and v
        # if roots are same, they are already in same set
        # else, merge smaller set to larger set using rank attribute to keep structure flat
        # return true if merged occur

        pu = self.find(u) # find grandparent
        pv = self.find(v) # find grandparent
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u,v in edges:
            if dsu.union(u, v):
                res -= 1
        return res

        