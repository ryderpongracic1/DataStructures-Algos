class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # explore decision tree
        def dfs(subset, idx):
            if idx == len(nums): # reached decision tree leaf node
                res.append(subset[:])
            elif idx < len(nums):
                dfs(subset, idx + 1) # exclude current num & explore
                subset.append(nums[idx]) # include current num
                dfs(subset, idx + 1) # explore inclusion branch
                subset.pop() # backtrack
        dfs([], 0)
        return res