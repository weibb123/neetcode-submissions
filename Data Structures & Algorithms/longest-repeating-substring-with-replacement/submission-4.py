class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # count frequency of characters
        # use set
        # res, keep track length of longest
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0 # counting frequency
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    
                    l += 1
                res = max(res, r - l + 1)
        
        return res

        
        