class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Have 2 pointers track the 2 strings
        # if s[i] == s[j] advance pointers
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == s[j]:
                i += 1
            # j advances
            j += 1
        return i == len(s) # went through all of string s
        