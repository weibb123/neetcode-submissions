class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        # credits, prerequisites
        # {0: [1,2], ...}
        hashmap = {i: [] for i in range(numCourses)}

        visiting = set()

        for crs, pre in prerequisites:
            hashmap[crs].append(pre)
        
        def dfs(crs):
            # return True if base case has
            # no prereq
            if hashmap[crs] == []:
                return True
            # there is a cycle
            if crs in visiting:
                return False
            
            visiting.add(crs)
            for pre in hashmap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            hashmap[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


        