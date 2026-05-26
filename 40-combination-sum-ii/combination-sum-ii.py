# - each element may be chosen at most 1x per combination
# - solution set contains no duplicate combinations
# - sort to have duplicates adjacent, faster pruning
# - dfs backtracking: 
#    - each element considered once per recursion level
#    - no reuse of elements (pass i + 1)
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []

        def dfs(curr, total, idx):
            if total == target:
                res.append(curr[:])
                return
            # for loop explores element for current slot in combination
            for i in range(idx, len(candidates)):
                # branch is a dead end
                if total + candidates[i] > target:
                    break
                # no reuse duplicate for CURRENT slot in current combination
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                curr.append(candidates[i])
                dfs(curr, total + candidates[i], i + 1)
                curr.pop()
        dfs([], 0, 0)
        return res