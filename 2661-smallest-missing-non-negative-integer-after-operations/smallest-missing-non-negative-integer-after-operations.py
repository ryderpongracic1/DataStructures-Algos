class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        count = [0] * value
        mex = 0

        # count remainders mod val
        for x in nums:
            count[x % value] += 1

        # find smallest missing non-negative num that we cannot form
        while count[mex % value] > 0:
            count[mex % value] -= 1
            mex += 1

        return mex
