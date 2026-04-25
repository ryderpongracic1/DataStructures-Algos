class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True) # start with closest to target
        stack = [] # finish times

        for pos, vel in cars:
            finish_time = (target - pos) / vel

            # faster/equal finish time would join same fleet
            # larger finish_time means slower fleet
            if not stack or finish_time > stack[-1]:
                stack.append(finish_time)

        return len(stack)