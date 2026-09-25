class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=len)
        dp = {w: 1 for w in words}
        res = 1

        for word in words:
            for i in range(len(word)):
                pred = word[:i] + word[i + 1:]
                if pred in dp:
                    dp[word] = max(dp[word], dp[pred] + 1)
                    res = max(res, dp[word])

        return res