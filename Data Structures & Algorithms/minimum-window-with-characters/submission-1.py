class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we need a dictionary to keep track of frequency
        # sliding window to change window size depending on the condition

        # edge case: return ""
        if t == "":
            return ""
        # we need to have two hashmap: countT, window
        countT, window = {}, {}
        # add frequency to countT from string t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # initialized how many we have, how many needed
        have, need = 0, len(countT)
        # res, resLen = [-1, -1], float(inf)
        res, resLen = [-1, -1], float("infinity")

        # initialized l = 0, for r loop to change window sliding
        l = 0
        for r in range(len(s)):
            c = s[r]
            # keep track of frequency of s[r]
            window[c] = 1 + window.get(c, 0)

            # if s[r] in countT and window[c] == countT[c]:
            # have add 1
            if s[r] in countT and window[c] == countT[c]:
                have += 1
            
            # when have == need
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # window[s[l]] -= 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""

        