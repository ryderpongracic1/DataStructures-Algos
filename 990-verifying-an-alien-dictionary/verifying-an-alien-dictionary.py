class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {}
        for idx, char in enumerate(order):
            alphabet[char] = idx

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if alphabet[w1[j]] > alphabet[w2[j]]:
                        return False
                    else:
                        break
        return True