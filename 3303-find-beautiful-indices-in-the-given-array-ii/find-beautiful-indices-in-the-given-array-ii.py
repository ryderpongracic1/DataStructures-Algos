class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def compute_lps(word):
            m = len(word)
            i = 1
            length = 0
            lps = [0] * m

            while i < m:
                if word[i] == word[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                elif length == 0:
                    lps[i] = 0
                    i += 1
                else:
                    length = lps[length - 1]
            return lps
        def kmp_search(text, pattern):
            n, m = len(text), len(pattern)
            indices = []
            lps = compute_lps(pattern)
            i = j = 0
            while i < n:
                if pattern[j] == text[i]:
                    j += 1
                    i += 1
                if j == m:
                    indices.append(i - j)
                    j = lps[j - 1]
                elif i < n and pattern[j] != text[i]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return indices

        indices_a, indices_b = kmp_search(s, a), kmp_search(s, b)
        res = []
        ptr_b = 0
        for i in indices_a:
            while ptr_b < len(indices_b) and indices_b[ptr_b] < i - k:
                ptr_b += 1
            if ptr_b < len(indices_b) and indices_b[ptr_b] <= i + k:
                res.append(i)
        return res