class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        # dp[i][j] means s[i:j + 1] is a palindromic substring
        dp = [[False] * n for _ in range(n)]

        # base case: 1 char is palindrome
        for i in range(n):
            dp[i][i] = True

        start = 0 # start idx of longest palindromic substring
        max_len = 1 # length of longest palindromic substring

        # increasing substring lengths from 2 chars to n (entire string)
        for length in range(2, n + 1):

            # last idx of substring given fixed length
            for i in range(n - length + 1):
                j = i + length - 1 # last idx of substring with fixed len
                if s[i] != s[j]:
                    dp[i][j] = False
                
                # s[i] == s[j]
                elif length == 2:
                    dp[i][j] = True
                else:
                    # s[i] == s[j],
                    # is the sub-substring s[i + 1: j] palindromic?
                    dp[i][j] = dp[i + 1][j - 1]

                # save longest palindromic substring
                if dp[i][j] and length > max_len:
                    start, max_len = i, length
        return s[start:start + max_len]