def caesar_cypher(text, shift=3, encrypt=True):
    result = ''
    for char in text:
        if char.isalpha():
            boundary_low, boundary_high = (ord('a'), ord('z')) if char.islower() else (ord('A'), ord('Z'))
            shift = -shift if not encrypt else shift
            shifted = ord(char) + shift
            if shifted > boundary_high: shifted -= 26
            if shifted < boundary_low: shifted += 26
            result += chr(shifted)
        else: result += char
    return result

plaintext = input("Enter a word or phrase to encrypt: ")
encrypted_text = caesar_cypher(plaintext)
decrypted_text = caesar_cypher(encrypted_text, encrypt=False)
print(f"\nOriginal: {plaintext}\nEncrypted: {encrypted_text}\nDecrypted: {decrypted_text}")
