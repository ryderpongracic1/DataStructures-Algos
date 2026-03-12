class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True) # Start at cars closes to finish line
        stack = [] # time to finish

        for pos, vel in cars:
            time = (target - pos) / vel
            if not stack or time > stack[-1]: # Later time to finish
                stack.append(time)

        return len(stack)