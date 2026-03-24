import hashlib
import base64
import time
import uuid
from datetime import datetime

# password = "AMADEUS"
# nonce = "secretnonce10111"
# timestamp = "2015-09-30T14:12:15Z"

password = "S7Np+Jbf*8NS"
message_id = str(uuid.uuid4())
nonce = message_id[24:]
timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

pass_sha = hashlib.sha1(
    nonce.encode("utf-8") + timestamp.encode("utf-8") + hashlib.sha1(password.encode("utf-8")).digest()
).digest()
pass_sha_encoded = base64.b64encode(pass_sha).decode("utf-8")
base64_nonce = base64.b64encode(nonce.encode("utf-8")).decode("utf-8")

print('message id: ' + message_id)
print('nonce_base64: ' + base64_nonce)
print('password_sha: ' + pass_sha_encoded)
print('timestamp: ' + timestamp)

# def _generate_x_signature():
#     public_key = '5b71dab131f0331cf4941d4adb71f97a'
#     private_key = '2c50e188fd'
#     utc_date = str(int(time.time()))
#     signature = hashlib.sha256(
#         (public_key + private_key + utc_date).encode('utf-8')
#     ).hexdigest()
#     return signature
#
#
# print('hotelbeds signature:' + _generate_x_signature())
