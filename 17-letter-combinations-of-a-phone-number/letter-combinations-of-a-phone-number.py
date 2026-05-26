class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        keypad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7':'pqrs', '8': 'tuv', '9': 'wxyz'}

        def dfs(curr, idx):
            if idx == len(digits):
                res.append(''.join(curr))
                return
            # traverse mapped characters of idx's digit
            for d in keypad[digits[idx]]:
                curr.append(d)
                dfs(curr, idx + 1)
                curr.pop()

        dfs([], 0)
        return res