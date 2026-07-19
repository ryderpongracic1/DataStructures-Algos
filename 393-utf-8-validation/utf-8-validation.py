class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i, n = 0, len(data)
        while i < n:
            num_bytes = self.num_bytes_for_leading(data[i])
            if num_bytes == -1: # not leading byte
                return False
            elif num_bytes + i > n: # not enough bytes left
                return False

            # check continuation bytes: data[i + 1:i + num_bytes]
            for j in range(i + 1, num_bytes + i):
                if not self.is_continuation(data[j]):
                    return False

            i += num_bytes # skip continuation bytes to next leading char
        return True
    def num_bytes_for_leading(self, byte):
        # mask byte with AND to check leading 1s & 0s
        if byte & 0b10000000 == 0: # 1-byte: 0xxxxxxxx
            return 1
        elif byte & 0b11100000 == 0b11000000: # 2-byte: 11xxxxxx
            return 2
        elif byte & 0b11110000 == 0b11100000: # 3-byte: 11100000
            return 3
        elif byte & 0b11111000 == 0b11110000: # 4-byte: 11110000
            return 4
        else:
            # continuation byte or larger than 4
            return -1
    def is_continuation(self, byte):
        return byte & 0b11000000 == 0b10000000