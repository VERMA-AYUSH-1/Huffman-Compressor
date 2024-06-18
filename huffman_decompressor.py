# def dectobin(decimal):
#     return bin(decimal)[2:].zfill(8)

# def huffman_decompress(input_file):
#     with open(input_file, 'rb') as file:
#         num_of_unique_chars = file.read(1)[0]

#         extension_length = int(file.read(1)[0])
#         extension = ''.join([file.read(1).decode('utf-8') for _ in range(extension_length)])

#         output_file = input_file.replace('-compressed.bin', f'-decompressed.{extension}')

#         decode_map = {}
#         while True:
#             char = file.read(1).decode('utf-8')
#             if char == '\0':
#                 break
#             code = ''
#             while True:
#                 bit = file.read(1).decode('utf-8')
#                 if bit == '\0':
#                     break
#                 code += bit
#             decode_map[code] = char

#         padding = int(file.read(1)[0])
#         file.read(1)
#         file.read(1)

#         encoded_data = ''
#         while byte := file.read(1):
#             encoded_data += dectobin(ord(byte))

#         encoded_data = encoded_data[padding:]

#         current_code = ''
#         with open(output_file, 'w') as output:
#             for bit in encoded_data:
#                 current_code += bit
#                 if current_code in decode_map:
#                     output.write(decode_map[current_code])
#                     current_code = ''

#     print("Decompressed File Successfully.")

# if __name__ == "__main__":
#     import sys
#     input_path = sys.argv[1]
#     huffman_decompress(input_path)




# def dectobin(decimal):
#     return bin(decimal)[2:].zfill(8)

# def huffman_decompress(input_file):
#     with open(input_file, 'rb') as file:
#         # Read number of unique characters in the original file
#         num_of_unique_chars = file.read(1)[0]

#         # Read extension length and extension type
#         extension_length = int(file.read(1)[0])
#         extension = ''.join([file.read(1).decode('utf-8') for _ in range(extension_length)])

#         # Construct output file path
#         output_file = input_file.replace('-compressed.bin', f'-decompressed.{extension}')

#         # Build the decode map from the compressed file
#         decode_map = {}
#         while True:
#             char = file.read(1).decode('utf-8')
#             if char == '\0':
#                 break
#             code = ''
#             while True:
#                 bit = file.read(1).decode('utf-8')
#                 if bit == '\0':
#                     break
#                 code += bit
#             decode_map[code] = char

#         # Read padding information
#         padding = int(file.read(1)[0])

#         # Skip the unused bytes
#         file.read(1)
#         file.read(1)

#         # Read the encoded data and remove padding
#         encoded_data = ''
#         while byte := file.read(1):
#             encoded_data += dectobin(ord(byte))

#         encoded_data = encoded_data[padding:]

#         # Decode the encoded data using the decode map
#         current_code = ''
#         with open(output_file, 'w') as output:
#             for bit in encoded_data:
#                 current_code += bit
#                 if current_code in decode_map:
#                     output.write(decode_map[current_code])
#                     current_code = ''

#     print("Decompressed File Successfully.")

# if __name__ == "__main__":
#     import sys
#     input_path = sys.argv[1]
#     huffman_decompress(input_path)


# def dectobin(decimal):
#     return bin(decimal)[2:].zfill(8)

# def huffman_decompress(input_file):
#     with open(input_file, 'rb') as file:
#         num_of_unique_chars = file.read(1)[0]

#         extension_length = int(file.read(1)[0])
#         extension = ''.join([chr(file.read(1)[0]) for _ in range(extension_length)])

#         output_file = input_file.replace(b'-compressed.bin', f'-decompressed.{extension}'.encode('utf-8').decode('utf-8'))

#         decode_map = {}
#         while True:
#             char = file.read(1).decode('utf-8')
#             if char == '\0':
#                 break
#             code = ''
#             while True:
#                 bit = file.read(1).decode('utf-8')
#                 if bit == '\0':
#                     break
#                 code += bit
#             decode_map[code] = char

#         padding = int(file.read(1)[0])

#         file.read(1)
#         file.read(1)

#         encoded_data = ''
#         while byte := file.read(1):
#             encoded_data += dectobin(ord(byte))

#         encoded_data = encoded_data[padding:]

#         current_code = ''
#         with open(output_file, 'w') as output:
#             for bit in encoded_data:
#                 current_code += bit
#                 if current_code in decode_map:
#                     output.write(decode_map[current_code])
#                     current_code = ''

#     print("Decompressed File Successfully.")

# if __name__ == "__main__":
#     import sys
#     input_path = sys.argv[1]
#     huffman_decompress(input_path)



# def dectobin(decimal):
#     return bin(decimal)[2:].zfill(8)

# def huffman_decompress(input_file):
#     with open(input_file, 'rb') as file:
#         num_of_unique_chars = file.read(1)[0]

#         extension_length = int(file.read(1)[0])
#         extension = ''.join([chr(file.read(1)[0]) for _ in range(extension_length)])

#         output_file = input_file.decode('utf-8', errors='ignore').replace('-compressed.bin', f'-decompressed.{extension}')

#         decode_map = {}
#         while True:
#             char = file.read(1).decode('utf-8', errors='ignore')
#             if char == '\0':
#                 break
#             code = ''
#             while True:
#                 bit = file.read(1).decode('utf-8', errors='ignore')
#                 if bit == '\0':
#                     break
#                 code += bit
#             decode_map[code] = char

#         padding = int(file.read(1)[0])

#         file.read(1)
#         file.read(1)

#         encoded_data = ''
#         while byte := file.read(1):
#             encoded_data += dectobin(ord(byte))

#         encoded_data = encoded_data[padding:]

#         current_code = ''
#         with open(output_file, 'w') as output:
#             for bit in encoded_data:
#                 current_code += bit
#                 if current_code in decode_map:
#                     output.write(decode_map[current_code])
#                     current_code = ''

#     print("Decompressed File Successfully.")

# if __name__ == "__main__":
#     import sys
#     input_path = sys.argv[1]
#     huffman_decompress(input_path)


def dectobin(decimal):
    return bin(decimal)[2:].zfill(8)

def huffman_decompress(input_file):
    with open(input_file, 'rb') as file:
        num_of_unique_chars = file.read(1)[0]
        extension_length = int(file.read(1)[0])
        extension = ''.join([chr(file.read(1)[0]) for _ in range(extension_length)])

        output_file = input_file.decode().replace('-compressed.bin', f'-decompressed.{extension}')

        decode_map = {}
        for _ in range(num_of_unique_chars):
            char = file.read(1).decode("utf-8")
            code_length = file.read(1)[0]
            code = ''.join([chr(file.read(1)[0]) for _ in range(code_length)])
            decode_map[code] = char

        padding = int(file.read(1)[0])

        encoded_data = ''
        while byte := file.read(1):
            encoded_data += dectobin(byte[0])

        encoded_data = encoded_data[:-padding]

        current_code = ''
        with open(output_file, 'w') as output:
            for bit in encoded_data:
                current_code += bit
                if current_code in decode_map:
                    output.write(decode_map[current_code])
                    current_code = ''

    print("Decompressed File Successfully.")

if __name__ == "__main__":
    import sys
    input_path = sys.argv[1]
    huffman_decompress(input_path)




# def dectobin(decimal):
#     return bin(decimal)[2:].zfill(8)

# def huffman_decompress(input_file):
#     with open(input_file, 'rb') as file:
#         # Read number of unique characters
#         num_of_unique_chars = file.read(1)[0]

#         # Read the length of the file extension
#         extension_length = file.read(1)[0]
#         # Read the file extension
#         extension = file.read(extension_length).decode()

#         # Create the output file path
#         output_file = input_file.replace(b'-compressed.bin', b'-decompressed.' + extension.encode())

#         # Read the Huffman codes
#         decode_map = {}
#         for _ in range(num_of_unique_chars):
#             char = file.read(1)
#             code_length = file.read(1)[0]
#             code = file.read(code_length).decode()
#             decode_map[code] = char

#         # Read the padding
#         padding = file.read(1)[0]

#         # Read the encoded data
#         encoded_data = ''
#         while byte := file.read(1):
#             encoded_data += dectobin(byte[0])

#         # Remove padding bits
#         encoded_data = encoded_data[:-padding]

#         # Decode the encoded data using the Huffman codes
#         current_code = ''
#         with open(output_file, 'wb') as output:
#             for bit in encoded_data:
#                 current_code += bit
#                 if current_code in decode_map:
#                     output.write(decode_map[current_code])
#                     current_code = ''

#     print("Decompressed File Successfully.")

# if __name__ == "__main__":
#     import sys
#     input_path = sys.argv[1]
#     huffman_decompress(input_path)
