class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combination = []

        def dfs(i, cur, total):
            if total == target:
                combination.append(cur.copy())
                return
            # backtrack to explore other options
            if total > target or i == len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()
            

            # identify and skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, cur, total)
        

        dfs(0, [], 0)
        return combination
        