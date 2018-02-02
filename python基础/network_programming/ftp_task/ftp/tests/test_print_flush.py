# n = 0
# while n < 3:
#     print(".", end="", flush=False)
#     n += 1
# n = 0
#
# n = 0
# f = open('a', 'wb')
# while n < 3:
#     try:
#         f.write('eeff'.encode('utf-8'))
#     except:
#         f.close()
#         raise
#     else:
#         n += 1
# f.flush()
# f.close()

import os

size = os.path.getsize('a')
print(size)
f = open('a', 'ab')
f.seek(size)
try:
    f.write('efg'.encode('utf-8'))

except:
    raise
finally:
    f.close()


