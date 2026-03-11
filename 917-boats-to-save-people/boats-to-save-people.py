class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        ans = 0
        people.sort()

        left = 0
        right = len(people) - 1
        while left <= right:
            boat = people[left] + people[right]
            if boat <= limit:
                left += 1
            right -= 1
            ans += 1
        return ans