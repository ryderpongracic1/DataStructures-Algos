class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        res = [[], []]
        losses = {}
        for w, l in matches:
            if w not in losses:
                losses[w] = 0
            losses[l] = 1 + losses.get(l, 0)

        no_loss, one_loss = [], []
        for player, loss_count in losses.items():
            if loss_count == 0:
                no_loss.append(player)
            elif loss_count == 1:
                one_loss.append(player)

        no_loss.sort()
        one_loss.sort()
        return [no_loss, one_loss]