class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word_count = 0  # Track number of words

    # Insert a word into the Trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        if not node.is_end_of_word:  # Prevent counting duplicates
            node.is_end_of_word = True
            self.word_count += 1

    # Count words in Trie
    def count_words(self):
        return self.word_count

# Example Usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")
trie.insert("apple")  # Duplicate word

print("Total Words in Trie:", trie.count_words())  # Output: 3
