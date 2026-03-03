from collections import defaultdict
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = unpaired = 0
        hset = {}
        for word in words:
            if word[0] == word[1]:
                if hset.get(word, 0) > 0:
                    unpaired -= 1
                    hset[word] -= 1
                    ans += 4
                else:
                    hset[word] = hset.get(word, 0) + 1
                    unpaired += 1
            else:
                reverse = word[::-1]
                if hset.get(reverse, 0) > 0:
                    hset[reverse] -= 1
                    ans += 4
                else:
                    hset[word] = hset.get(word, 0) + 1
        if unpaired > 0:
            ans += 2
        return ans