class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str):
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOfWord = True

    def search(self, word:str):
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children
        return curr.isEndOfWord
    
    def startsWith(self, prefix:str):
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr.children[c]
        return True
        
            
