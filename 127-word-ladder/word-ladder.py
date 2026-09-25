from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(list) # 'd*g' -> ['dog', 'dig', ...]
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                code = word[:i] + '*' + word[i + 1:]
                adj[code].append(word)

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            curr, steps = queue.popleft()
            if curr == endWord:
                return steps
            for i in range(len(curr)):
                code = curr[:i] + '*' + curr[i + 1:]
                for n in adj[code]:
                    if n not in visited:
                        visited.add(n)
                        queue.append((n, steps + 1))
                adj[code] = [] # clear
        return 0