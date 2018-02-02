
import hashlib
import base64


def getmd5(strings):
    temp_bytes = strings.encode('utf-8')
    m = hashlib.sha256()
    m.update(temp_bytes)
    return m.hexdigest()


def encrypt(src_str):
    encoded = base64.b64encode(src_str.encode('utf-8'))
    return encoded.decode('utf-8')


def decrypt(str_encoded):
    str_encoded = str_encoded.encode('utf-8')
    data = base64.b64decode(str_encoded)
    return data.decode('utf-8')


