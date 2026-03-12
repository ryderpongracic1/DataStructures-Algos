class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for char in path.split('/'):
            if char == '..':
                if stack:
                    stack.pop()
            elif char and char != '.':
                stack.append(char)

        return '/' + '/'.join(stack)