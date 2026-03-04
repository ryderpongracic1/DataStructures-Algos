class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(len(s)):
            if dp[i]: # dp[0] == True
                for word in wordDict:
                    n = len(word)
                    if i + n <= len(s) and s[i : i + n] == word:
                        dp[i + n] = True
        return dp[len(s)]