import hashlib
import time

def _generate_x_signature_dev():
    public_key = '5b71dab131f0331cf4941d4adb71f97a'
    private_key = '2c50e188fd'
    utc_date = str(int(time.time()))
    signature = hashlib.sha256(
        (public_key + private_key + utc_date).encode('utf-8')
    ).hexdigest()
    return signature


print('hotelbeds signature:' + _generate_x_signature_dev())