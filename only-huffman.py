from huffman import HuffmanCoding

path = "input.txt"

# Huffmann Compression
h = HuffmanCoding(path)
output_path = h.compress()
print("Compressed file path: " + output_path)

"""
#Huffmann decompression
decom_path = h.decompress(output_path)
"""