class Solution:
    def defangIPaddr(self, address: str) -> str:
        newStr = []
        for char in address:
            if char != '.':
                newStr.append(char)
            else:
                newStr.append('[.]')
        return ''.join(newStr)