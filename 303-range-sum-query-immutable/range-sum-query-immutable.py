'''
NOTES
val[l:r] = prefix[r + 1] - val[left]
nums =   [-2, 0, 3, -5, 2, -1]
prefix = [-2, -2, 1, -4, -2, -3]
sum(nums[1:3]) inclusive = 0 + 3 + -5 = -2
        = prefix[3] - prefix[0] = -4 - -2 = -2
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)