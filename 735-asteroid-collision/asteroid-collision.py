class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            if not stack:
                stack.append(a)
            else:
                while stack and stack[-1] > 0 and a < 0:
                    if abs(a) > abs(stack[-1]):
                        stack.pop()
                    elif abs(stack[-1]) == abs(a):
                        stack.pop()
                        a = 0
                    else: # 
                        a = 0
                if a != 0:
                    stack.append(a)
        return stack