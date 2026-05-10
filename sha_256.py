import hashlib
def sha256_hash(message):
# Convert string to bytes
    message_bytes = message.encode('utf-8')
# Create SHA-256 object
    sha256 = hashlib.sha256()
# Update hash object
    sha256.update(message_bytes)
# Get hexadecimal digest
    return sha256.hexdigest()
# Example usage
text = "Hello World"
hash_value = sha256_hash(text)
print("Original Text:", text)
print("SHA-256 Hash:", hash_value)  