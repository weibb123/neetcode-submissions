class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # brute force
        # fleet = fast car catch up to slow car then same speed together
        # we want to return number of fleets
        # faster car = fast velocity will catch up low velocity car
        # sort position array in close -> farthest order
        # if time > stack[-1], this car never reach fleet ahead
        # so we push a new fleet
        # if time < stack[-1], this car is fast.
        car = sorted(zip(position, speed), reverse=True)

        stack = []

        for pos, spd in car:
            # step 2: compute time
            time = (target - pos) / spd

            # step 3: can tis car catch the fleet ahead?
            # time must be < stack[-1] top of stack
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)



        