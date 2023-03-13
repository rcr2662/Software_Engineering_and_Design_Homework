
def customEncrypt(inputText, N, D):
    reverse_text = inputText[::-1]
    ascii_reverse = []
    encoded_chars = []
    for char in reverse_text:
        ascii_reverse.append(ord(char))

    count = 0
    for i in ascii_reverse:
        if D == 1:
            encoded_chars.append(chr(ascii_reverse[count] + N))
        else:
            encoded_chars.append(chr(ascii_reverse[count] - N))
        count +=1

    cypher_text = ''.join(encoded_chars)
    return cypher_text
