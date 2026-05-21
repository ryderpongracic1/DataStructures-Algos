class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # explore decision tree
        def dfs(subset, idx):
            res.append(subset[:])
            for i in range(idx, len(nums)):
                subset.append(nums[i]) # include current num
                dfs(subset, i + 1) # explore branch
                subset.pop() # backtrack
        dfs([], 0)
        return res