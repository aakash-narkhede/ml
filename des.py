from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
# 8-byte key
key = b'8bytekey'
cipher = DES.new(key, DES.MODE_ECB)
# Encryption
plaintext = "IMCAimr"
padded_text = pad(plaintext.encode(), DES.block_size)
ciphertext = cipher.encrypt(padded_text)
print("Encrypted:", ciphertext)
# Decryption
decipher = DES.new(key, DES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), DES.block_size)
print("Decrypted:", decrypted.decode())
