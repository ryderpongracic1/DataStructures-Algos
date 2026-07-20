class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(i, j):
            while i > -1 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            # loop breaks when s[i] != s[j] => return last good slice
            return s[i + 1: j]

        res = ''
        for i in range(len(s)):
            odd, even = isPalindrome(i, i), isPalindrome(i, i + 1)

            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        return res