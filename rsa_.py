import math
# Step 1: Choose two prime numbers
p = 61
q = 53
# Step 2: Compute n
n = p * q
# Step 3: Compute phi(n)
phi = (p - 1) * (q - 1)
# Step 4: Choose e (public key)
e = 17 # must be coprime with phi
# Step 5: Compute d (private key)
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None
d = mod_inverse(e, phi)
print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))
# Step 6: Encryption
MESSAGE = 65 # Plaintext (must be < n)
CIPHER = pow(MESSAGE, e, n)
print("Encrypted message:", CIPHER)
# Step 7: Decryption
DECRYPTED = pow(CIPHER, d, n)
print("Decrypted message:", DECRYPTED)