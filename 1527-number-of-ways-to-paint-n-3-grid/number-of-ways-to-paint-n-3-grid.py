class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        brb = 6
        rgb = 6
        for _ in range(1, n):
            brb, rgb = (
                (3 * brb + 2 * rgb) % MOD,
                (2 * brb + 2 * rgb) % MOD
            )

        return (rgb + brb) % MOD