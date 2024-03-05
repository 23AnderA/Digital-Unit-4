class VigenereCipher:

    def __init__(self, keyword):
        self.keyword = keyword

    @staticmethod
    def _char_shift(char, shift):
        if 'a' <= char <= 'z':
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            return char

    def _keyword_shift(self, index):
        keyword_char = self.keyword[index % len(self.keyword)]
        return ord(keyword_char.lower()) - ord('a')

    def encrypt(self, plaintext):
        ciphertext = ''
        for i, char in enumerate(plaintext):
            shift = self._keyword_shift(i)
            ciphertext += self._char_shift(char, shift)
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''
        for i, char in enumerate(ciphertext):
            shift = -self._keyword_shift(i)
            plaintext += self._char_shift(char, shift)
        return plaintext

if __name__ == "__main__":
    user_keyword = input("Enter the keyword: ")
    user_text = input("Enter the text to encrypt: ")

    cipher = VigenereCipher(user_keyword)
    encrypted = cipher.encrypt(user_text)

    print(f"Encrypted: {encrypted}")

    # Uncomment below if you also want to show the decrypted text
    # decrypted = cipher.decrypt(encrypted)
    # print(f"Decrypted: {decrypted}")
