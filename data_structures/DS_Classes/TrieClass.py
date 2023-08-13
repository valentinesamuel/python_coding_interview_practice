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
        """
        create a string array and run the recursive
        function to populate the array with all
        the strings in the trie
        """
        strings = []
        self._get_total_words(self.root, [], strings)
        return strings

    def total_words_length(self):
        """
        return the length of the total_words array
        """
        return len(self.total_words())

    def sort_trie(self):
        words = self.total_words()
        return self._quick_sort(words)

    def _quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        LHS = [word for word in arr if word < pivot]
        MID = [word for word in arr if word == pivot]
        RHS = [word for word in arr if word > pivot]

        return self._quick_sort(LHS) + MID + self._quick_sort(RHS)

    def _get_total_words(self, node: TrieNode, string: list, strings: list):
        """
        if the current node is the end of a word,
        join all the previous nodes as a single word
        and add them to the strings array
        then for every character in the children of
        the current node, append the node to the current
        string being made and recursively call the function
        starting from the children at the current character,
        then pop the last item on the string
        """
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
print(trie.sorted_total_words())
