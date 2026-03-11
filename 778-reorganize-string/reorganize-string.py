import heapq
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        elements = {}

        for char in s:
            elements[char] = elements.get(char, 0) + 1

        heap = []
        for char, freq in elements.items():
            heapq.heappush(heap, (-freq, char))
        
        prev = None
        ans = []
        while heap or prev:
            if not heap and prev:
                return ''

            freq, char = heapq.heappop(heap)
            ans.append(char)

            if prev:
                heapq.heappush(heap, prev)
                prev = None
            
            freq += 1
            if freq < 0:
                prev = (freq, char)
        return ''.join(ans)