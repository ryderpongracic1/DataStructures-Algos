#   |j - i| <= k
# -> -k <= j - i <= k
# -> i - k <= j <= i + k
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        # Builds Longest Prefix Suffix array for KMP
        # (longest prefix that is also a suffix)
        def compute_lps(pattern):
            m = len(pattern)
            lps = [0] * m
            length = 0 # of previous longest prefix suffix
            i = 1

            while i < m:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        # Finds all starting indices of pattern in text
        def kmp_search(text, pattern):
            n, m = len(text), len(pattern)
            if m == 0:
                return []
            lps = compute_lps(pattern)
            indices = []
            i = j = 0

            while i < n:
                if pattern[j] == text[i]:
                    i += 1
                    j += 1
                if j == m:
                    indices.append(i - j)
                    j = lps[j - 1]
                elif i < n and pattern[j] != text[i]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return indices
        
        indices_a = kmp_search(s, a)
        indices_b = kmp_search(s, b)

        res = []
        ptr_b = 0
        m = len(indices_b)

        for i in indices_a:
            # advance j until indices_b[ptr_b] is at least lower bound of (i - k)
            while ptr_b < m and i - k > indices_b[ptr_b]:
                ptr_b += 1

            # check if valid ptr_b also satiesfies upper bound of (i + k)
            if ptr_b < m and indices_b[ptr_b] <= k + i:
                res.append(i)

        return res