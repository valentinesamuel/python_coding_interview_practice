from DS_Classes.TrieClass import Trie

import sys
sys.path.append('../DS_Classes/')


def is_formation_possible(dictionary: list, target: str):
    trie = Trie()

    for word in dictionary:
        trie.insert(word)

    for i in range(len(target)):
        prefix = target[:i+1]
        suffix = target[i+1:]

        if trie.search(prefix) and trie.search(suffix):
            return True

    return False

dictionary = ["web", "application", "tech", "companies"]
target_word = "webtech"
print(is_formation_possible(dictionary, target_word)) 