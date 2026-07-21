class Solution:
    def longestPrefix(self, s: str) -> str:
        m = len(s)
        lps = [0] * m
        i = 1
        length = 0
        while i < m:
            # match: advance both ptrs
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1

            # mismatch with prev match: try shorter
            elif length != 0:
                length = lps[length - 1]

            # mismatch with no prev match
            else:
                lps[i] = 0
                i += 1

        if lps[-1] == 0:
            return ''
        return s[:lps[-1]]