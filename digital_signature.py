import rsa

# Step 1: Generate keys
public_key, private_key = rsa.newkeys(512)

# Step 2: Message
message = input("Enter message: ")

# Step 3: Create digital signature
signature = rsa.sign(message.encode(), private_key, 'SHA-256')
print("Digital Signature:", signature)

# Step 4: Verify signature
try:
    rsa.verify(message.encode(), signature, public_key)
    print("Signature Verified")
except rsa.VerificationError:
    print("Signature Verification Failed")
