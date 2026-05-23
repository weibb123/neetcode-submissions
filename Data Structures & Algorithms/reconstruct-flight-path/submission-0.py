class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # set up adjancy list
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"] # starting
        def dfs(src):
            # finish if..
            if len(tickets) + 1 == len(res):
                return True
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i, v)
                res.pop()
            return False
        
        dfs("JFK")
        return res
        