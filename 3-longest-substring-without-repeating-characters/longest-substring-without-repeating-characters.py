class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        maxLen = 0
        left = 0
        for right in range(len(s)):
            if s[right] not in letters:
                letters.add(s[right])
                maxLen = max(maxLen, right - left + 1)
            else:
                while s[right] in letters:
                    letters.remove(s[left])
                    left += 1
                letters.add(s[right])
        return maxLen