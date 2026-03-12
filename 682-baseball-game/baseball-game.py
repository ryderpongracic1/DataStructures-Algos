class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        total = 0
        for op in operations:
            if op == 'C':
                total -= stack.pop()
            elif op == '+':
                total += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                total += stack[-1] * 2
                stack.append(stack[-1] * 2)
            else: # op == digit
                stack.append(int(op))
                total += int(op)
        
        return total
