class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        seenVowels = []
        for i in range(len(s)):
            if s[i] in vowels:
                seenVowels.append(s[i])

        ans = ''
        counter = -1
        for i in range(len(s)):
            if s[i] in vowels:
                ans += seenVowels[counter]
                counter -= 1
            else:
                ans += s[i]
        return ans