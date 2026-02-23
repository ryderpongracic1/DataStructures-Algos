class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        ans = []
        for num in nums:
            if num not in elements:
                elements[num] = 1
            else:
                elements[num] += 1
        
        numbers = list(elements)
        frequencies = list(elements.values())
        sortedFrequencies = list(zip(frequencies, numbers))
        sortedFrequencies.sort(reverse=True)
        for i in range(k):
            ans.append(sortedFrequencies[i][1])
        return ans