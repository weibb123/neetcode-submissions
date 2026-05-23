class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = set()
        l = 0
        result = 0

        # two cases: either s[r] in hashmap or not
        for r in range(len(s)):
            # if s[r] in hashmap
            while s[r] in hashmap:
                hashmap.remove(s[l])
                l += 1
            hashmap.add(s[r])
            result = max(result, r - l + 1)
        
        return result

        