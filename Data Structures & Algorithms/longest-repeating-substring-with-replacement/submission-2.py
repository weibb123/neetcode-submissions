class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # change window size if not valid
        # if valid keep expanding window

        l = 0
        maxf = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]]) # get max freq char

            # not valid: len(window) - maxfreq > k
            if (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
        
        return (r-l+1)



        