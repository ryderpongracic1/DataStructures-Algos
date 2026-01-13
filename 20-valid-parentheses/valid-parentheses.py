class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closed = "]})"
        stack = []
        for char in s:
            if char not in closed:
                stack.append(char)
            else:
                if stack:
                    openChar = stack.pop()
                    if openChar == '{':
                        if char != '}':
                            return False
                    elif openChar == '(':
                        if char != ')':
                            return False
                    else:# openChar == '['
                        if char != ']':
                            return False
                else:
                    return False
        return len(stack) == 0