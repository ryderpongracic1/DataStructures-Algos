class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        noteSet = {}
        for char in ransomNote:
            if char not in noteSet:
                noteSet[char] = 1
            else:
                noteSet[char] += 1
        magSet = {}
        for char in magazine:
            if char in ransomNote:
                if char not in magSet:
                    magSet[char] = 1
                else:
                    magSet[char] += 1
        for letter, freq in noteSet.items():
            if letter not in magSet:
                return False
            if freq > magSet[letter]:
                return False
        return True
        