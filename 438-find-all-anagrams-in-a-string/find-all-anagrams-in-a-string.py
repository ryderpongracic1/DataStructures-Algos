class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pCount = [0] * 26
        seen = [0] * 26
        ans = []
        for char in p:
            pCount[ord(char) - ord('a')] += 1
        left = 0
        for right in range(len(s)):
            seen[ord(s[right]) - ord('a')] += 1
            if right - left + 1 > len(p):
                seen[ord(s[left]) - ord('a')] -= 1
                left += 1
            if seen == pCount:
                ans.append(left)
        return ans