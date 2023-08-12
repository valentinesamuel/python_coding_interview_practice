class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """insert a new word into the trie:\n
        for every char in the word, if the char not
        children of the current node, then create and
        trienode for the char, if it is the children,
        mark the end of the word as true
        """
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOfWord = True

    def search(self, word: str):
        """search for a word in the trie:\n
        for every char in the word, if the char not
        children of the current node, return false, 
        otherwise, move to the next trienode and
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

    def startsWith(self, prefix: str):
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

    def total_words(self):
        strings = []
        self._get_total_words(self.root, [], strings)
        return strings
    
    def total_words_lenngth(self):
        return len(self.total_words())

    def _get_total_words(self, node: TrieNode, string: list, strings: list):
        if node.isEndOfWord:
            strings.append("".join(string))
        for ch in node.children:
            string.append(ch)
            self._get_total_words(node.children[ch], string, strings)
            string.pop()


trie = Trie()
trie.insert('the')
trie.insert('there')
trie.insert('answer')
trie.insert('any')
trie.insert('by')
trie.insert('bye')
trie.insert('their')
trie.insert('education')
trie.insert('educative')
print(trie.total_words_lenngth())
