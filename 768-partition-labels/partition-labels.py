class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []

        last_seen = [-1] * 26
        for i, char in enumerate(s):
            last_seen[ord(char) - ord('a')] = i
        
        left = right = 0
        for i, char in enumerate(s):
            right = max(right, last_seen[ord(char) - ord('a')])

            if i == right:
                ans.append(right - left + 1)
                left = i + 1

        return ans
