class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()

            curr = curr.children[char]
        
        curr.end = True

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.end

            char = word[i]

            if char == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True

                return False
            
            if char not in node.children:
                return False

            return dfs(node.children[char], i + 1)
        
        return dfs(self.root, 0)
        
        
