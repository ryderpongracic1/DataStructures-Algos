class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(s) < len(p):
            return ans

        pfreq = [0] * 26
        for char in p:
            pfreq[ord(char) - ord('a')] += 1

        window = [0] * 26
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[ord(char) - ord('a')] += 1
            if right - left + 1 > len(p): # Window is larger than p
                remove = ord(s[left]) - ord('a')
                window[remove] -= 1
                left += 1

            if window == pfreq:
                ans.append(left)
        return ans