# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ""
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_word = True
            node.word = word

        def replace(word):
            node = root
            for ch in word:
                if ch not in node.children or node.is_word:
                    break
                node = node.children[ch]
            return node.word if node.is_word else word

        return " ".join(map(replace, sentence.split()))