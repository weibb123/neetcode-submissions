class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Mapping of digits to corresponding letters
        phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }

        def backtrack(index, path):
            # when index reaches the end of digit
            if index == len(digits):
                res.append(path)
                return
            possible_letter = phone_map[digits[index]]
            for letter in possible_letter:
                backtrack(index+1, path + letter)

        res = []
        backtrack(0, "")
        return res

        