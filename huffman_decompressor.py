
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



