from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
# AES requires 16, 24, or 32 byte key
key = b'1234567890abcdef' # 16 bytes = AES-114
# Generate random IV (Initialization Vector)
iv = get_random_bytes(16)
# Create AES cipher object (CBC mode)
cipher = AES.new(key, AES.MODE_CBC, iv)
# -------- Encryption --------
plaintext = "Aakash Narkhede"
padded_text = pad(plaintext.encode(), AES.block_size)
ciphertext = cipher.encrypt(padded_text)
print("Encrypted (Base64):", base64.b64encode(ciphertext).decode())
# -------- Decryption --------
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_padded = decipher.decrypt(ciphertext)
decrypted = unpad(decrypted_padded, AES.block_size)
print("Decrypted Text:", decrypted.decode())