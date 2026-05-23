class Solution:
    def isValid(self, s: str) -> bool:
        # valid parentheses: ()
        stack = []
        # close in on top of the stack
        CloseToOpen = { ")": "(", 
                        "}": "{",
                        "]": "["}

        # stack[-1] is (, CloseToOpen[')'] -> (
        for char in s:
            if char in CloseToOpen:
                if stack and stack[-1] == CloseToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        # return true if stack is gone
        return True if not stack else False
        