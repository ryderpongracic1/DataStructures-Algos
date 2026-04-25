from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, left = 0, 0
        freq = defaultdict(int)
        most = 0 # most frequent char (others in substr get replaced)

        for right in range(len(s)):
            char = s[right]
            freq[char] += 1
            most = max(most, freq[char])
            
            if right - left + 1 - most > k:
                remove = s[left]
                freq[remove] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans