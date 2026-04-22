class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lefts = [1] * n
        rights = [1] * n
        ans = [1] * n

        for i in range(1, n):
            lefts[i] = lefts[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            rights[i] = rights[i + 1] * nums[i + 1]

        for i in range(n):
            ans[i] = lefts[i] * rights[i]
        return ans