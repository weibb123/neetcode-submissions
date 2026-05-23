class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # set up adjancy list
        flight_map = collections.defaultdict(list)
        result = []
        
        for src, dst in tickets:
            flight_map[src].append(dst)
        
        # sort within the hastmap
        for dst in flight_map:
            flight_map[dst].sort(reverse=True)
       
       # DFS traversal
        def dfs(src):
            dst = flight_map[src]

            # traverse all destinations
            while dst:
                next_dst = dst.pop()
                dfs(next_dst)

            result.append(src)
        dfs("JFK")
        return result[::-1]
        