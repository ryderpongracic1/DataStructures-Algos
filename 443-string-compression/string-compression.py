class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0  # scanner to find group size
        write = 0 # udpates chars in-place

        while read < len(chars):
            letter = chars[read] # save letter bc it may be overwritten
            count = 0 # track group size
            # scan until group breaks
            while read < len(chars) and chars[read] == letter:
                read += 1
                count += 1

            chars[write] = letter # save char regardless of group-size
            write += 1

            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        return write