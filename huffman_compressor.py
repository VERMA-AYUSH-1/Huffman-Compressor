
import heapq
import os
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequency):
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", code_map={}):
    if node:
        if node.char is not None:
            code_map[node.char] = prefix
        generate_codes(node.left, prefix + "0", code_map)
        generate_codes(node.right, prefix + "1", code_map)
    return code_map

def huffman_compress(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    root = build_huffman_tree(frequency)

    huffman_codes = generate_codes(root)

    encoded_text = ''.join(huffman_codes[char] for char in text)

    padding = 8 - len(encoded_text) % 8
    encoded_text = encoded_text + '0' * padding

    b = bytearray()
    for i in range(0, len(encoded_text), 8):
        byte = encoded_text[i:i+8]
        b.append(int(byte, 2))

    with open(output_file, 'wb') as file:
        file.write(bytes([len(huffman_codes)]))

        for char, code in huffman_codes.items():
            file.write(char.encode('utf-8'))
            file.write(bytes([len(code)]))
            file.write(code.encode('utf-8'))

        file.write(bytes([padding]))

        file.write(bytes(b))

if __name__ == "__main__":
    import sys
    input_path = sys.argv[1]
    output_path = input_path.replace('.txt', '-compressed.bin')
    huffman_compress(input_path, output_path)
