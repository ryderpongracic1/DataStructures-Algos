class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sub = 0
        curr = 0
        while sub < len(s) and curr < len(t):
            if s[sub] == t[curr]:
                sub += 1
                curr += 1
            else:
                curr += 1
        if sub == len(s):
            return True
        else:
            return False