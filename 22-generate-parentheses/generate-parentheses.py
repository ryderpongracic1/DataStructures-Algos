class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtrack(opens, closes, curr):
            if len(curr) == n * 2:
                ans.append(''.join(curr))
                return
            if opens < n:
                curr.append('(')
                backtrack(opens + 1, closes, curr)
                curr.pop()
            
            if closes < opens:
                curr.append(')')
                backtrack(opens, closes + 1, curr)
                curr.pop()
        backtrack(0, 0, [])
        return ans