import hashlib

m = hashlib.sha256()
m.update(b'admin123')
r = m.hexdigest()
print(r,len(r))
