import hashlib


def calc_md5(data_bytes):
    m = hashlib.sha256()
    m.update(data_bytes)
    return m.hexdigest()

username = 'Alex'
password = '123'

tmp = ('%s%s' % (username, password)).encode('utf-8')
md5 = calc_md5(tmp)
print(md5)

usermd5 = calc_md5(username.encode('utf-8'))



