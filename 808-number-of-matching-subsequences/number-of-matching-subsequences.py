class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = collections.defaultdict(list)
        for word in words:
            it = iter(word)
            waiting[next(it)].append(it) # bucket by next-needed char (first)

        res = 0
        for c in s:

            # dict.pop(key, default) REMOVES key from dict & returns val
            #   if key present, else returns default
            advancing = waiting.pop(c, []) # all words waiting for c
            for w in advancing:

                # next(iter, default) pulls next iter, or default if none
                nxt = next(w, None) # advance c until end of word
                if nxt is None:
                    res += 1
                else:
                    waiting[nxt].append(w)

        return res