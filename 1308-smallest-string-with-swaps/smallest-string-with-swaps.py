class UnionFind:
    def __init__(self):
        self.parent = {} # idx -> parent idx
        self.rank = {} # idx -> size of component

    def add(self, idx):
        if idx not in self.parent:
            self.parent[idx] = idx
            self.rank[idx] = 1

    def find(self, idx):
        if self.parent[idx] != idx:
            self.parent[idx] = self.find(self.parent[idx])
        return self.parent[idx]

    def union(self, idx1, idx2):
        root1, root2 = self.find(idx1), self.find(idx2)

        if root1 == root2:
            return
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root1] = root2
            self.rank[root2] += 1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind()
        for i in range(len(s)):
            uf.add(i)
        for idx1, idx2 in pairs:
            uf.union(idx1, idx2)

        root_to_chars = collections.defaultdict(list)
        for i in range(len(s)):
            root = uf.find(i)
            root_to_chars[root].append(s[i])

        for chars in root_to_chars.values():
            chars.sort(reverse=True)

        res = []
        for i in range(len(s)):
            root = uf.find(i)
            res.append(root_to_chars[root].pop())

        return ''.join(res)