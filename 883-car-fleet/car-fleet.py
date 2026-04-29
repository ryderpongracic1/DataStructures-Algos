class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = []

        for pos, vel in cars:
            hours_to_finish = (target - pos) / vel

            # Car makes new fleet if finishes slower
            if not stack or hours_to_finish > stack[-1]:
                stack.append(hours_to_finish)
            # if hours_to_finish <= car infront it joins their fleet at their speed
        
        return len(stack)
