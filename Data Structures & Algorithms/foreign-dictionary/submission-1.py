class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # map every character to a set as values
        adj = {c: set() for w in words for c in w}

        # compare adjacent word to find first differing char between them
        # Add an edge w1[j] -> w2[j] 
        # since the first mismatch determines the relative order of the characters.
        # Edge Case: If a longer word (w1) precedes a shorter word (w2) 
        # but their prefixes match, the input is invalid (e.g., ["abcd", "abc"]), so return ""
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            # check first character different
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = {} # keep track of visited node
        res = [] # list to store toplogical order
        def dfs(char):
            if char in visit:
                return visit[char] # return True if a cycle detected
            
            visit[char] = True # mark as visiting

            for neighChar in adj[char]:
                if dfs(neighChar): # recursively visit neighbors
                    return True # cycle detected
            
            visit[char] = False # mark as fully processed
            res.append(char) # add to result list
        
        for char in adj:
            if dfs(char):
                return "" # detect a loop, return empty string
        
        res.reverse()
        return "".join(res)


        