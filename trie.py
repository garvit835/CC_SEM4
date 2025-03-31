class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the Trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    # Search for a word in the Trie
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    # Helper function for remove
    def _remove(self, node, word, depth):
        if depth == len(word):
            if node.is_end_of_word:
                node.is_end_of_word = False
            return len(node.children) == 0  # If no children, delete node
        
        char = word[depth]
        if char not in node.children:
            return False  # Word not found

        should_delete = self._remove(node.children[char], word, depth + 1)

        if should_delete:
            del node.children[char]
            return len(node.children) == 0 and not node.is_end_of_word
        
        return False

    # Remove a word from the Trie
    def remove(self, word):
        self._remove(self.root, word, 0)

# Example Usage
trie = Trie()
trie.insert("apple")
trie.insert("app")

print(trie.search("apple"))  # True
print(trie.search("app"))    # True

trie.remove("apple")
print(trie.search("apple"))  # False
print(trie.search("app"))    # True
