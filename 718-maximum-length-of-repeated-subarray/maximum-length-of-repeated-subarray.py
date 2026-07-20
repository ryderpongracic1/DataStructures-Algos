class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        prev = [0] * (m + 1)
        res = 0

        for i in range(1, n + 1):
            curr = [0] * (m + 1)
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                    res = max(res, curr[j])
            prev = curr

        return res