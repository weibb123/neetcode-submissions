class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # new result array
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index(days)]

        for i, t in enumerate(temperatures):

            # stack[-1][0] = temperature on top of stack
            while stack and t > stack[-1][0]: # if found temp greater than on top of stack
                stackT, stackDay = stack.pop()
                res[stackDay] = i - stackDay
            stack.append((t, i))
        return res


        