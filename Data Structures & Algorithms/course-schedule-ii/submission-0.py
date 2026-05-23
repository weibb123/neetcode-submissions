class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            hashmap[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            # base case
            if crs in visit:
                return True
            
            if crs in cycle:
                return False
            
            cycle.add(crs)
            for pre in hashmap[crs]:
                if dfs(pre) == False:
                    return False

            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output



        