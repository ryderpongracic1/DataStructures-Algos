class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        alphabet = {} # char -> position
        for i, c in enumerate(order):
            alphabet[c] = i
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j] != word2[j]:
                    if alphabet[word1[j]] < alphabet[word2[j]]:
                        break
                    # else:
                    return False
        return True