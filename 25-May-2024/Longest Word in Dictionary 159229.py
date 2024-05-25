# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        for word in sorted(words):
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.end_of_word = True

        self.res = ""
        self.dfs(root, "")
        return self.res

    def dfs(self, node, path):
        if len(path) > len(self.res) or (len(path) == len(self.res) and path < self.res):
            self.res = path
        for ch in node.children:
            if node.children[ch].end_of_word:
                self.dfs(node.children[ch], path + ch)