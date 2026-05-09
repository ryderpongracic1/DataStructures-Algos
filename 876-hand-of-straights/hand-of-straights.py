import heapq
from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = defaultdict(int)
        for card in hand:
            freq[card] += 1
        
        cards = sorted(list(freq.keys()))

        for card in cards:
            count = freq[card]
            if count == 0:
                continue
            
            for i in range(groupSize):
                if count > freq[card + i]: # more smaller-nums than needed-nums
                    return False
                freq[card + i] -= count # used count-times

        return True