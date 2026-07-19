class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        res = [[], []]
        players = set() # all players with less than 2 losses
        losses = collections.defaultdict(int) # player -> num losses

        for w, l in matches:
            players.add(w)
            players.add(l)
            losses[l] += 1

        for p in sorted(players):
            if losses[p] == 0:
                res[0].append(p)
            elif losses[p] == 1:
                res[1].append(p)

        return res