import heapq

# Huffman Tree Node
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

# Build Huffman Tree
def build_huffman_tree(frequency):
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

# Generate Huffman Codes
def generate_codes(node, code="", huffman_dict={}):
    if node:
        if node.char is not None:
            huffman_dict[node.char] = code
        generate_codes(node.left, code + "0", huffman_dict)
        generate_codes(node.right, code + "1", huffman_dict)
    return huffman_dict

# Encode text using Huffman codes
def huffman_encode(text):
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    root = build_huffman_tree(frequency)
    huffman_dict = generate_codes(root)

    encoded_text = "".join(huffman_dict[char] for char in text)
    return encoded_text, huffman_dict, root

# Decode Huffman encoded text
def huffman_decode(encoded_text, root):
    decoded_text = ""
    node = root

    for bit in encoded_text:
        node = node.left if bit == "0" else node.right

        if node.char:
            decoded_text += node.char
            node = root

    return decoded_text

# Example Usage
text = "hello huffman"
encoded_text, huffman_dict, root = huffman_encode(text)

print("Huffman Codes:", huffman_dict)
print("Encoded Text:", encoded_text)
print("Decoded Text:", huffman_decode(encoded_text, root))
