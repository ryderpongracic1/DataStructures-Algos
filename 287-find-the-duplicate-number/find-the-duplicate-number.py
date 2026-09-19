class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # array as linked list: i -> nums[i]
        # each val [1, n] 
        #  -> every val points to valid idx
        #  -> no val points to 0
        slow = fast = nums[0]

        # tortoise and hare cycle-finding
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow