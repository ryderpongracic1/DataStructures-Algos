class TrieNode:
    def __init__(self):
        self.children = {} # char -> TrieNode
        self.word = None # end of word marker

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word
        
        ROWS, COLS = len(board), len(board[0])
        ans, seen = set(), set()
        
        def backtrack(r, c, node):
            # invalid board bounds
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in seen:
                return

            # non-match character
            if board[r][c] not in node.children:
                return
            
            # board[r][c] guaranteed to match character
            seen.add((r, c))
            node = node.children[board[r][c]]

            if node.word:
                ans.add(node.word)
                node.word = None
            
            backtrack(r + 1, c, node)
            backtrack(r - 1, c, node)
            backtrack(r, c + 1, node)
            backtrack(r, c - 1, node)

            seen.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, root)
        return list(ans)