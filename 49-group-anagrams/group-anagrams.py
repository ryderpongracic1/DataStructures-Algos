class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = collections.defaultdict(list) # hashed anagram -> words
        for s in strs:
            word = [0] * 26
            for c in s:
                word[ord('a') - ord(c)] += 1
            anagrams[tuple(word)].append(s)

        return list(anagrams.values())