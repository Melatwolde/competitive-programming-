# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        return self._search_in_node(word, self.root)

    def _search_in_node(self, word: str, node: Node) -> bool:
        for i, ch in enumerate(word):
            if ch not in node.children:

                if ch == '.':
                    for x in node.children.values():
                        if self._search_in_node(word[i + 1:], x):
                            return True
                return False
          
            else:
                node = node.children[ch]
        return node.is_word
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)