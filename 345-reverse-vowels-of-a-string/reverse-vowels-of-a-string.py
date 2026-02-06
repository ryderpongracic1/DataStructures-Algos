class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        newStr = list(s)
        left = 0
        right = len(newStr) - 1
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                newStr[left], newStr[right] = newStr[right], newStr[left]
                left += 1
                right -= 1
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
        return ''.join(newStr)