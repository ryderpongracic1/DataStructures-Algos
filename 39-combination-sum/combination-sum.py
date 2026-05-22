class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(curr, total, idx):
            if total == target:
                res.append(curr[:])
                return
            for i in range(idx, len(candidates)):
                if total + candidates[i] > target:
                    break
                curr.append(candidates[i])
                dfs(curr, total + candidates[i], i)
                curr.pop()

        dfs([], 0, 0)
        return res