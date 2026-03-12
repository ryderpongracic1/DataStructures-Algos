class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matches = {']':'[', ')':'(', '}':'{'}
        stack = []
        for c in s:
            if c in matches:
                if not stack or matches[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return not stack