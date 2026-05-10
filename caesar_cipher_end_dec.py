text = input("Enter text: ")
shift = int(input("Enter shift value: "))
# Encryption
encrypted = ""
for i in text:
    encrypted += chr(ord(i) + shift)
print("Encrypted text:", encrypted)
# Decryption
decrypted = ""
for i in encrypted:
    decrypted += chr(ord(i) - shift)
print("Decrypted text:", decrypted)
