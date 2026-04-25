class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = [] # (start idx, height)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                pop_idx, pop_h = stack.pop()
                ans = max(ans, pop_h * (i - pop_idx))
                start = pop_idx

            stack.append((start, h))

        for idx, h in stack:
            ans = max(ans, h * (len(heights) - idx))
        return ans