class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        freq1 = {}
        for num in nums1:
            freq1[num] = freq1.get(num, 0) + 1
        freq2 = {}
        for num in nums2:
            freq2[num] = freq2.get(num, 0) + 1
        
        for num1, frequency in freq1.items():
            if num1 in freq2:
                if frequency > freq2[num1]:
                    ans += [num1] * freq2[num1]
                else:
                    ans += [num1] * frequency

        return ans