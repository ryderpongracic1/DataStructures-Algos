class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        # Look-up tables for irregular numbers
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine","Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
            "Seventy", "Eighty", "Ninety"]

        scale = ['', 'Thousand', 'Million', 'Billion']

        def helper(n):
            if n == 0:
                return ''
            elif n < 20:
                return below_20[n] + ' '
            elif n < 100:
                # peels tens digit & recurses on remainder
                return tens[n // 10] + ' ' + helper(n % 10)
            else:
                # peels hundred digit & recurses on 2-digit remainder
                return below_20[n // 100] + ' Hundred ' + helper(n % 100)

        res = ''
        i = 0
        while num > 0:
            # skip handles xx, 000, xxx case
            if num % 1000 != 0:
                # num % 1000 to get 3 rightmost digits
                res = helper(num % 1000) + scale[i] + ' ' + res

            # num // 1000 to remove 3 rightmost digits
            num //= 1000
            i += 1 # trackes scale & increments per 000 chunk

        return res.strip()