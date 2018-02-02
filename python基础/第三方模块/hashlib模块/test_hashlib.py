# -*- coding: utf-8 -*-
"""
hashlib的构造函数都是类似的，返回的对象拥有相同的接口。
如sha256()构造了sha-256对象，使用Update()将bytes字节来填充sha-256对象
在任何时刻都可以调用digest()或者hexdigest()来获取加密后的数据

注意： 不支持将字符串对象输入到update()中，因为hash会以字节(bytes)为单位，而不是以字符为单位。
"""
import hashlib

m = hashlib.sha256()
# m.update("我是李志平")
# 会报错，TypeError: Unicode-objects must be encoded before hashing
m.update("我是李志平".encode('utf-8')) # 必须要转成字节bytes类型
# m.update("wosliuzhipeng") 会报错TypeError: Unicode-objects must be encoded before hashing
m.update(b"wosliuzhipeng")
# 或者m.update("wosliuzhipeng".encode('utf-8'))
print(m.hexdigest())
# m.h
