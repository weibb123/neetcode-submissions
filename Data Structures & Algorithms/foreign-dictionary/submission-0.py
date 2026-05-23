class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # map every character to a set
        adj = {c: set() for w in words for c in w}


        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            # check first character different
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # add to adjacency list
                    adj[w1[j]].add(w2[j])
                    break
        

        visit = {}
        res = []

        def dfs(char):
            if char in visit:
                return visit[char]
            
            visit[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True
            
            visit[char] = False
            res.append(char)
        
        for char in adj:
            if dfs(char):
                return "" # detect a loop
        
        res.reverse()
        return "".join(res)


        