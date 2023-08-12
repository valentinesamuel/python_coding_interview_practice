class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str):
        """insert a new word into the trie:\n
        for every char in the word, if the char not
        children of the current node, then create a trienode for the char, if it is the children, mark the end of the word as true
        """
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOfWord = True

    def search(self, word:str):
        """search for a word in the trie:\n
        for every char in the word, if the char not
        children of the current node, return false, otherwise, move to the next trienode and
        finally return the value os the end-of-word-ness

        Args:
            val (str|int): integer or string
        """
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isEndOfWord
    
    def startsWith(self, prefix:str):
        """
        for every char in the word, if the
        children char of the current node
        does not contain the char return
        false, else return true
        """
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        
            
