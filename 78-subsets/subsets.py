class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(subset, idx):
            # choose current valid subset
            res.append(subset[:])
            # try every num once per recursion level
            for i in range(idx, len(nums)):
                subset.append(nums[i]) # include i
                dfs(subset, i + 1) # explore path
                subset.pop() # backtrack

        dfs([], 0)
        return res