class Node:
    def __init__(self) -> None:
        self.children = [Node] * 26
        self.isEnd = False


class Trie:
    def __init__(self) -> None:
        self.root = self.getNode()

    def getNode() -> Node:
        return Node()

    def makeIndex(self, ch):
        return ord(ch)-ord('a')

    def insert(self, word):
        root = self.root
        for char in word:
            index = self.makeIndex(char)
            if not root.children[index]:
                root.children[index] = self.getNode()
            root = root.children[index]
        root.isEnd = True

    def search(self, word):
        root = self.root
        for char in word:
            index = self.makeIndex(char)
            if not root.children[index]:
                return False
            root = root.children[index]
        return root.isEnd


class Solution:
    def build(self, words):
        # Fill this in.
        self.tree = Trie()
        [self.tree.insert(word) for word in words]

    def autocomplete(self, word):
        # Fill this in.
        pass
    

s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge'])
print(s.autocomplete('do'))
# ['dog', 'door', 'dodge']
