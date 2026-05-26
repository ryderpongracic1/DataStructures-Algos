class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(curr, idx):
            res.append(curr[:])
            for i in range(idx, len(nums)):
                # avoid duplicates for the same slot (same recursion lvl)
                # avoid searching redundant trees
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                dfs(curr, i + 1)
                curr.pop()

        dfs([], 0)
        return res