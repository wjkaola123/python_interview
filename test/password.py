import hashlib
import base64

password = "S7Np+Jbf*8NS"
nonce = "YGx5V1h5cEw="
timestamp = "2024-01-04T03:28:09Z"

# password = "AMADEUS"
# nonce = "secretnonce10111"
# timestamp = "2015-09-30T14:12:15Z"

pass_sha = hashlib.sha1(
    nonce.encode("utf-8") + timestamp.encode("utf-8") + hashlib.sha1(password.encode("utf-8")).digest()
).digest()
pass_sha_encoded = base64.b64encode(pass_sha).decode("utf-8")

print(pass_sha_encoded)