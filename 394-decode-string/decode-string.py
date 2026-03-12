class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] # (prev string, multiplier)
        curr, num = '', 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == ']':
                prev, multiplier = stack.pop()
                curr = prev + (curr * multiplier)
            elif char == '[':
                stack.append((curr, num))
                curr, num = '', 0
            else:
                curr += char
        return curr