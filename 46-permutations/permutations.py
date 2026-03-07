class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        visited = [False] * len(nums)
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            for i in range(len(nums)):
                # Already in curr
                if visited[i]:
                    continue
                
                # Choose i to add
                visited[i] = True
                curr.append(nums[i])

                # Explore
                backtrack(curr)

                # Backtrack: remove from curr and mark not seen
                visited[i] = False
                curr.pop()
        backtrack([])
        return ans