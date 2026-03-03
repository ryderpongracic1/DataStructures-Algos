class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        if len(s) < len(p):
            return ans

        pfreq = {}
        for char in p:
            pfreq[char] = pfreq.get(char, 0) + 1
        
        window = {}
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if right - left + 1 > len(p): # Window is larger than p
                remove = s[left]
                window[remove] -= 1
                if window[remove] == 0:
                    del window[remove]
                left += 1
                
            if window == pfreq:
                ans.append(left)
        return ans