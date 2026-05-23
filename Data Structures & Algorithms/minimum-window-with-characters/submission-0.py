class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # two hashmap
        # pop left window until have != need
        # add right window until have == need

        if t == "": return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0) # add letters from string t
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('infinity')
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0) # add letters from string s

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from left window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
            

        