class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        # lookup tables
        below_20 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six',
            'Seven','Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen',
            'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
            'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
            'Seventy', 'Eighty', 'Ninety']
        scale = ['', 'Thousand', 'Million', 'Billion']

        # Convert n (0-999) to words
        def helper(n):
            # zero is blank in words
            if n == 0:
                return ''

            # n is 1-19
            # always outputs num + space for potential scalar
            # eg 'One ' + 'Thousand'
            elif n < 20:
                return below_20[n] + ' '

            # n is 20 - 99
            elif n < 100:
                #      tens amount   + ones amount
                # ex: 23: 23 // 10 = 2, 23 % 10 = 3
                # tens[2] = 'Twenty'
                # helper(3) = 'Three '
                return tens[n // 10] + ' ' + helper(n % 10)

            # n is 100-999
            else:
                # n / 100: strip 3 digit num to 1 digit
                # n % 100: get 2 rightmost digits
                return below_20[n // 100] + ' Hundred ' + helper(n % 100)
        
        res = ''
        i = 0 # tracks scale ((1-999), thousand, million,...)
        while num > 0:
            # skip 000 in nums like xx, 000, xxx
            if num % 1000 != 0:
                # num % 1000: get 3 rightmost digits
                res = helper(num % 1000) + scale[i] + ' ' + res

            num //= 1000 # strip 3 rightmost digits
            i += 1 # advance scale

        return res.strip()
