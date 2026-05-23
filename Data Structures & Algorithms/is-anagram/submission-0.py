class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # two hashmap
        map_s, map_t = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            map_s[s[i]] = 1 + map_s.get(s[i], 0)
            map_t[t[i]] = 1 + map_t.get(t[i], 0)
        
        return map_s == map_t

        