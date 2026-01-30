class Solution:
    def defangIPaddr(self, address: str) -> str:
        newStr = ''
        for char in address:
            if char != '.':
                newStr += char
            else:
                newStr += '[.]'
        return newStr