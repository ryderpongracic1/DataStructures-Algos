class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(curr, total, idx):
            # base case 1: answer
            if total == target:
                res.append(curr[:])
                return

            # each candidate tried once per recursion level
            for i in range(idx, len(candidates)):
                # prune impossbile answers (sorted nums)
                if total + candidates[i] > target:
                    break
                curr.append(candidates[i])
                # passing i (not i + 1) lets reuse in deeper recursion levels
                dfs(curr, total + candidates[i], i)

                # restores curr so next i can explore diff branch
                curr.pop()
        
        dfs([], 0, 0)
        return res