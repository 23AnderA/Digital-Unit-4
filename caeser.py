def caesar_encrypt(text, shift=3):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted += chr(shifted)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift=3):
    decrypted = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted += chr(shifted)
        else:
            decrypted += char
    return decrypted

# Prompt the user
plaintext = input("Enter a word or phrase to encrypt: ")

encrypted_text = caesar_encrypt(plaintext)
decrypted_text = caesar_decrypt(encrypted_text)

print("\nOriginal:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)