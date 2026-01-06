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

        for char in magazine:
            if char in noteSet:
                noteSet[char] -= 1
                if noteSet[char] == 0:
                    del noteSet[char]
            if not noteSet:
                return True
        return False
        