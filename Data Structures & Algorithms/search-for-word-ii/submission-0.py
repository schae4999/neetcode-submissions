class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()

        # Build trie from all words
        for word in words:
            curr = root 

            for char in word:
                if char not in curr.children:
                    curr.children[char] = Node()
                
                curr = curr.children[char]
            
            curr.end = True
            curr.word = word

        visited = set()
        result = set()

        def dfs(row, col, node):
            if (row, col) in visited:
                return

            char = board[row][col]

            if char not in node.children:
                return

            node = node.children[char]

            if node.end:
                result.add(node.word)

            visited.add((row, col))

            if row > 0:
                dfs(row - 1, col, node)
            if row < len(board) - 1:
                dfs(row + 1, col, node)
            if col > 0:
                dfs(row, col - 1, node)
            if col < len(board[0]) - 1:
                dfs(row, col + 1, node)
            
            visited.remove((row, col))

        # starting point in the board
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, root)

        return list(result)
            