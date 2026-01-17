class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == '#' and stack:
                stack.pop()
            else:
                if char != '#':
                    stack.append(char)
        s = ''.join(stack)

        stack = []
        for char in t:
            if char == '#' and stack:
                stack.pop()
            else:
                if char != '#':
                    stack.append(char)
        t = ''.join(stack)
        return s == t