class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def palindrome(s):
            return (s==s[::-1])
        
        def backtrack(start, path):
            # base case
            if start == len(s):
                result.append(path[:])
                return
            
            for end in range(start + 1, len(s)+1):
                substring = s[start:end]
                if palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop() # backtrack

        result = []
        backtrack(0, [])
        return result
        