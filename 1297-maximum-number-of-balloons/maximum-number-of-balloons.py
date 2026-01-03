class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        hset = {'b': 0, 'a': 0,'l': 0,'o': 0,'n': 0}
        for char in text:
            if char in hset:
                hset[char] += 1
    
        least = float('inf')
        for letter, frequency in hset.items():
            if letter == 'o' or letter == 'l':
                frequency //= 2
            least = min(least,frequency)
        return least