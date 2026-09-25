class Solution:
    def countPalindromes(self, s: str) -> int:
        MOD = 10**9 + 7
        ans = 0
        
        right_cnt = [0] * 10
        right_pair = [[0] * 10 for _ in range(10)]
        
        # 1. Precompute all pairs for the right side
        for char in s:
            d = int(char)
            # A new digit 'd' creates pairs with all previously seen digits
            for i in range(10):
                right_pair[i][d] += right_cnt[i]
            right_cnt[d] += 1
            
        left_cnt = [0] * 10
        left_pair = [[0] * 10 for _ in range(10)]
        
        # 2. Sweep to treat each character as the center 'c' of "d1 d2 c d2 d1"
        for char in s:
            d = int(char)
            
            # Remove current character from right-side counts
            right_cnt[d] -= 1
            for i in range(10):
                # The pairs broken are those starting with 'd' and ending 
                # with any character 'i' that is still on the right
                right_pair[d][i] -= right_cnt[i]
                
            # Count valid length-5 palindromes centered at 'd'
            for d1 in range(10):
                for d2 in range(10):
                    # left pair is (d1, d2), right pair must be (d2, d1)
                    ans = (ans + left_pair[d1][d2] * right_pair[d2][d1]) % MOD
                    
            # Add current character to left-side counts
            for i in range(10):
                left_pair[i][d] += left_cnt[i]
            left_cnt[d] += 1
            
        return ans